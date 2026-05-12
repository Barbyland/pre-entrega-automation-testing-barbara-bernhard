from selenium.webdriver.common.by import By


from utils.saucedemo_helpers import (
    add_first_product_to_cart,
    get_brand_title,
    get_first_product,
    get_inventory_title,
    login,
    open_cart,
)


def test_login_exitoso_redirige_al_inventario(driver):
    login(driver)

    assert "/inventory.html" in driver.current_url
    assert get_inventory_title(driver) == "Products"
    assert get_brand_title(driver) == "Swag Labs"


def test_catalogo_muestra_productos_y_elementos_principales(driver):
    login(driver)

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    _, primer_nombre, primer_precio = get_first_product(driver)

    assert get_inventory_title(driver) == "Products"
    assert len(productos) > 0
    assert primer_nombre != ""
    assert primer_precio.startswith("$")
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()


def test_agregar_primer_producto_al_carrito(driver):
    login(driver)

    nombre_producto, _ = add_first_product_to_cart(driver)
    contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert contador_carrito.text == "1"

    open_cart(driver)
    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    nombres_carrito = [
        producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        for producto in productos_carrito
    ]

    assert len(productos_carrito) == 1
    assert nombre_producto in nombres_carrito
