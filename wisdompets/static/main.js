function changeBackgroundColor()
{
    var mainDivId = "MainDiv";
    var colorInputId = "colorInput";

    var colorToSet = document.getElementById(colorInputId).value;
    document.getElementById(mainDivId).style.backgroundColor = colorToSet;
}