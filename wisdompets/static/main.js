function changeBackgroundColor() {
    var mainDivId = "MainDiv";
    var colorInputId = "colorInput";

    var colorToSet = document.getElementById(colorInputId).value;
    document.getElementById(mainDivId).style.backgroundColor = colorToSet;
}

function CreateAnimal() {
    var name = document.getElementById("input1").value;
    var breed = document.getElementById("input2").value;

    window.location.href = "localhost:8000/adoptions/pets/insert/$(name)/$(breed)/";
    console.log("localhost:8000/adoptions/pets/insert/$(name)/$(breed)/");
}