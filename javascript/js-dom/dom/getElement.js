/**
 * Created by lth on 17-4-18.
 */

// getElementById
alert(typeof document.getElementById("purchases"));

// getElementByTagName
var items = document.getElementsByTagName("li");
for (var i = 0; i < items.length; i++) {
    alert(typeof items[i])
}

var shopping = document.getElementById("purchases");
var items2 = shopping.getElementsByTagName("*");
alert(items.length);
for(var i = 0; i < items.length; i++) {
    alert(typeof items2[i]);
}

// getElementByClassName
var sales = shopping.getElementsByClassName("sale");
alert(sales.length);

function getElementsByClassName1(node, classname) {
    if (node.getElementsByClassName1) {
        return node.getElementsByClassName1(classname);
    } else {
        var results = new Array();
        var elems = node.getElementsByTagName("*");
        for (var i = 0; i < elems.length; i++) {
            if (elems[i].className.indexOf(classname) != -1) {
                results[results.length] = elems[i];
            }
        }
        return results;
    }

}