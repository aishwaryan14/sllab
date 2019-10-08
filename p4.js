function b1(){
var x=document.getElementById("number").value
if(isNaN(x)) throw document.getElementById("para").innerHTML="Not a number";
else{
	n=x*2;
	document.getElementById("para").innerHTML=n;
  }
}

function b2(){
var x=document.getElementById("number").value
if(isNaN(x)) throw document.getElementById("para").innerHTML="Not a number";
else{
	n=x*x;
	document.getElementById("para").innerHTML=n;
}
}

