let productId = $('#prod-id').val();
let token = $('input[name = csrfmiddlewaretoken]').val();
const minBtn = document.getElementById("minus-btn")
let numberOfQty = parseInt(document.getElementById('numberOfQty').value, 10);
numberOfQty = isNaN(numberOfQty) ? 0 : numberOfQty;

jQuery('#numberOfQty').keyup(function () { 
    this.value = this.value.replace(/[^0-9]/g,'1');
    this.value = this.value.replace(/^[0]+/g,'1');
    this.value = this.value.replace(/^[-0]+/g,'1');
});

function increment() {
    console.log("clicked")
    numberOfQty++;
    document.getElementById('numberOfQty').value = numberOfQty;

    if (numberOfQty > 0 ) minBtn.disabled = false;
}

function decrement() {
    numberOfQty--;
    document.getElementById('numberOfQty').value = numberOfQty;

    if (numberOfQty == 0 ) minBtn.disabled = true;
}

$('#size input').on('change', function() {
    console.log($('input[name=size]:checked', '#size').val())
}),

$('#add-btn').click(function () {
    location.reload(true);

    let currCount = $( "#numberOfQty").val();
    let size = $('input[name=size]:checked', '#size').val()

    $.ajax({
        method: "POST",
        url: "/addtocart",
        data: {
            "product_id": productId,
            "quantity": currCount,
            "size": size,
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