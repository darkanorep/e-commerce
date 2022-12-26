const minBtn = document.getElementById("minus-btn")
let quantity = document.getElementById("quantity")
let count = 1;
let currentCount = 1;

function increment() {
    currentCount++;
    count += 1;
    quantity.textContent = count;
}

function decrement() {
    if (count == 0) {
        minBtn.disabled = true;
    } else if (count == 1){
        minBtn.disabled = false;
    }else {
        currentCount--;
        count -= 1;
        quantity.textContent = count;   
    }
}

$('#add-btn').click(function () {

    let productId = $('#prod-id').val();
    let currCount = $( "#numberOfQty").val(currentCount).val();
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

