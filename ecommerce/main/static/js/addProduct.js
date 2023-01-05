let productId = $('#prod-id').val();
let token = $('input[name = csrfmiddlewaretoken]').val();

const minBtn = document.getElementById("minus-btn")
let numberOfQty = parseInt(document.getElementById('numberOfQty').value, 10);
numberOfQty = isNaN(numberOfQty) ? 0 : numberOfQty;

function increment() {
    numberOfQty++;
    document.getElementById('numberOfQty').value = numberOfQty;

    if (numberOfQty > 0 ) minBtn.disabled = false;
}

function decrement() {
    numberOfQty--;
    document.getElementById('numberOfQty').value = numberOfQty;

    if (numberOfQty == 0 ) minBtn.disabled = true;
}


$('#add-btn').click(function () {
    
    location.reload(true);
        
    let currCount = $( "#numberOfQty").val();

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

    alert("Add to cart success")

})

$('#add-rvw').submit(function () {
    let comment = $('textarea#comment').val();
    let review_img = $("#fileinput").val();
    console.log(review_img)
    $.ajax({
        method: "POST",
        url: "/addreview",
        data: {
            "product_id": productId,
            "comment": comment,
            csrfmiddlewaretoken: token
        },
        dataType: 'dataType',
        success: function(response) {
            console.log("add to review yarn")
        }
    })
    console.log("add to cart yarn")
})