/**
 * Created by lth on 17-4-18.
 */
// get attribute
var paras = document.getElementsByTagName("p");
for (var i = 0; i < paras.length; i++) {
    alert(paras[i].getAttribute("title"));
}

for (var i = 0; i < paras.length; i++) {
    var title_text = paras[i].getAttribute("title");
    if (title_text != null) {
        alert(title_text);
    }
}

// set attribute
var shopping = document.getElementById("purchases");
shopping.setAttribute("title", "a list of goods");

var shopping = document.getElementById("purchases");
alert(shopping.getAttribute("title"));