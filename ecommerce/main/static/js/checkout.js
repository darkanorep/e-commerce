let checkboxes = document.getElementsByName('item[]');
let vals = "";
let total = document.getElementById("total");


let selectItem = []

for (var i=0; i<checkboxes.length; i++) {
    if (checkboxes[i].checked) {
        vals += ","+checkboxes[i].value;
        // console.log(Number(checkboxes[i].value))
    }
    selectItem.push(Number(checkboxes[i].value))
    // console.log(price)
}
if (vals) vals = vals.substring(1);

//quantity of item
var qty = document.getElementsByName("quantity[]");
let quantity = []

for (var i=0; i<qty.length; i++) {
    if (qty[i]) {
        // console.log(Number(qty[i].innerText))
        quantity.push(Number(qty[i].innerText))
    }
}


let totals = (selectItem, quantity) => {
    return selectItem.map((e, index) => e * quantity[index]);
}

// console.log(totals(selectItem, quantity));
// console.log(
//     totals(selectItem, quantity).reduce((a, b) => a + b, 0)
// )

total.textContent = totals(selectItem, quantity).reduce((a, b) => a + b, 0)

