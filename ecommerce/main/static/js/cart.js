let checkboxes = document.getElementsByName('item[]');
let totalss = document.getElementById("total");

let selectItem = [];
let quantity = [];

for (var i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
        selectItem.push(Number(checkboxes[i].value));
        let qty = document.getElementsByName("quantity[]")[i];
        quantity.push(Number(qty.innerText));
    }
}

function total() {
    let computedTotal = 0;
    for (var i = 0; i < selectItem.length; i++) {
        computedTotal += selectItem[i] * quantity[i];
    }
    totalss.textContent = computedTotal;
}
total();
setInterval(function () {
    total();
}, 1000);

let token = $('input[name = csrfmiddlewaretoken]').val();

$(".increment-btn").click(function () {
    let productId = this.id.split('-')[0];
    let numberOfQty = parseInt(document.getElementById(`${productId}-numberOfQty`).value, 10);
    $(`#${productId}-numberOfQty`).val(numberOfQty + 1);
    $(`#${productId}-quantity`).text(numberOfQty + 1);
    
    $.ajax({
        method: "POST",
        url: "/updatecart",
        data: {
            "item_id": productId,
            "quantity": 1,
            csrfmiddlewaretoken: token
        },
        success: function(response) {
            console.log("add to cart");
            total();
        }
    });
});


$(".decrement-btn").click(function () {
    let itemID = this.value.split('-')[0]
    let productId = this.id.split('-')[0]
    let numberOfQty = parseInt(document.getElementById(`${productId}-numberOfQty`).value, 10);
    let itemId = parseInt(document.getElementById(`${itemID}-item`).value, 10);
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
            url: "/updatecart",
            data: {
                "item_id": productId,
                "quantity": -1,
                csrfmiddlewaretoken: token
            }
        });
    }
    
})

fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  // new
  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    
    // Get Checkout Session ID
    fetch("/create_checkout_session/")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
    
  });
});