function calculatePrice(fruitName, grams, pricePerKg) {
    let weigth = (grams / 1000).toFixed(2);
    let totalPrice = ((grams  * pricePerKg) / 1000).toFixed(2);

    console.log(`I need $${totalPrice} to buy ${weigth} kilograms ${fruitName}.`);
}

// calculatePrice('orange', 2500, 1.80);
// calculatePrice('apple', 1563, 2.35);
