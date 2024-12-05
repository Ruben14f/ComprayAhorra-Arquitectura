function decreaseQuantity() {
    const input = document.getElementById('quantity-input');
    const currentValue = parseInt(input.value) || 1; // Si está vacío, toma 1
    if (currentValue > 1) {
        input.value = currentValue - 1;
    }
}

function increaseQuantity() {
    const input = document.getElementById('quantity-input');
    const currentValue = parseInt(input.value) || 1; // Si está vacío, toma 1
    input.value = currentValue + 1;
}