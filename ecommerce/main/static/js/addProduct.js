const minBtn = document.getElementById("minus-btn")

function increment() {
    let numberOfQty = parseInt(document.getElementById('numberOfQty').value);
    numberOfQty = isNaN(numberOfQty) ? 0 : numberOfQty;
    numberOfQty++;
    document.getElementById('numberOfQty').value = numberOfQty;

    if (numberOfQty > 0 ) minBtn.disabled = false;
}

function decrement() {
    let numberOfQty = parseInt(document.getElementById('numberOfQty').value, 10);
    numberOfQty = isNaN(numberOfQty) ? 0 : numberOfQty;
    numberOfQty--;
    document.getElementById('numberOfQty').value = numberOfQty;

    if (numberOfQty == 0 ) minBtn.disabled = true;
}

$('#add-btn').click(function () {

    console.log("add to cart")

    let productId = $('#prod-id').val();
    let currCount = $( "#numberOfQty").val();
    let token = $('input[name = csrfmiddlewaretoken]').val();

    $.ajax({
        method: "POST",
        url: "/addtocart",
        data: {
            "product_id": productId,
            "quantity": currCount,
            csrfmiddlewaretoken: token
        },
        dataType: 'dataType',
        success: function(response) {
            console.log("add to cart")
        }
    })

})