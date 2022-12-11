var checkboxArray = [];

function addCheckboxName(checkbox) {
  if (checkbox.checked) {
    checkboxArray.push(checkbox.id);
    var node = document.createElement("div");
    node.setAttribute("class", "selected-symptom-tile");
    node.setAttribute("id", `tile-${checkbox.id}`);

    var text = document.createElement("label");
    text.innerText = checkbox.id
    node.appendChild(text)

    var parentNode = document.querySelector(".selected-symptoms");
    parentNode.appendChild(node);
  }else{
    checkboxArray = checkboxArray.filter((item) => item != checkbox.id)

    var node = document.getElementById(`tile-${checkbox.id}`);
    node.parentNode.removeChild(node);
  }
}

function predict(){
    document.forms["symptomForm"].submit();
}
