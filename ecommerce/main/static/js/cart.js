let checkboxes = document.getElementsByName('item[]');
let vals = "";
let totalss = document.getElementById("total");

let selectItem = []

for (var i=0; i<checkboxes.length; i++) {
    if (checkboxes[i].checked) {
        vals += ","+checkboxes[i].value;
        // console.log(Number(checkboxes[i].value))
    }
    selectItem.push(Number(checkboxes[i].value))
}
if (vals) vals = vals.substring(1);

//quantity of item
var qty = document.getElementsByName("quantity[]");
let quantity = []

for (var i=0; i<qty.length; i++) {
    if (qty[i]) {
        quantity.push(Number(qty[i].innerText))
    }
}

function total() {
    let totals = (selectItem, quantity) => {
        return selectItem.map((e, index) => e * quantity[index]);
    }

    let computedTotal = totals(selectItem, quantity).reduce((a, b) => a + b, 0)
    totalss.textContent = computedTotal
    
}
total()

let token = $('input[name = csrfmiddlewaretoken]').val();

$(".increment-btn").click(function () {
    let productId = this.id.split('-')[0]
    let numberOfQty = parseInt(document.getElementById(`${productId}-numberOfQty`).value, 10);
    // numberOfQty = isNaN(numberOfQty) ? 0 : numberOfQty;
    $(`#${productId}-numberOfQty`).val(numberOfQty + 1)
    $(`#${productId}-quantity`).text(numberOfQty + 1);
    
    $.ajax({
        method: "POST",
        url: "/addtocart",
        data: {
            "product_id": productId,
            "quantity": 1,
            csrfmiddlewaretoken: token
        },
        dataType: 'dataType',
        success: function(response) {
            console.log("add to cart")
            
        }
    })
})



$(".decrement-btn").click(function () {
    let productId = this.id.split('-')[0]
    let numberOfQty = parseInt(document.getElementById(`${productId}-numberOfQty`).value, 10);
    let itemId = parseInt(document.getElementById(`${productId}-item`).value, 10);
    // numberOfQty = isNaN(numberOfQty) ? 0 : numberOfQty;
    $(`#${productId}-numberOfQty`).val(numberOfQty - 1)
    $(`#${productId}-quantity`).text(numberOfQty - 1);

    if (numberOfQty == 1 ) {
        // minBtn.disabled = true;
        $.ajax({
            method: "GET",
            url: `/cart/remove/${itemId}`
        })
        location.reload(true);
    } else {
        $.ajax({
            method: "POST",
            url: "/addtocart",
            data: {
                "product_id": productId,
                "quantity": -1,
                csrfmiddlewaretoken: token
            }
        })
    }
    
})