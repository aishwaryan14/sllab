function submit(){
var x=document.getElementById("text").value
if(isNaN(x)){
	alert("Enter a number");
}
else if(x=="") throw document.getElementById("para").innerHTML="No number entered";

else if(x%3==0 && x%7==0){
	document.getElementById("para").innerHTML="Divisible by 3 and 7"
}
else if(x%3==0){
	document.getElementById("para").innerHTML="Divisible by 3"
}
else if(x%7==0){
	document.getElementById("para").innerHTML="Divisible by 7"
}
else{
	document.getElementById("para").innerHTML="Not Divisibe by 3 or 7"
}

}
