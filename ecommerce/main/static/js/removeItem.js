$('#remove-btn').click(function () {

    let itemId = $('#item-id').val();
    let token = $('input[name = csrfmiddlewaretoken]').val();

    $.ajax({
        method: "POST",
        url: "/removeitem",
        data: {
            "item_id": itemId,
            csrfmiddlewaretoken: token
        },
        dataType: "dataType",
        success: function(response) {
            console.log("removed")
        }

    })
})