function res(){
 var x=parseInt(document.getElementById("num1").value)
 var y=parseInt(document.getElementById("num2").value) 

 if(document.getElementById("add").checked){
 document.getElementById("para").innerHTML=x+y}
 
 else if(document.getElementById("sub").checked){
 document.getElementById("para").innerHTML=x-y} 
 
 else if(document.getElementById("mul").checked){
 document.getElementById("para").innerHTML=x*y} 
 
 else if(add.checked==false && sub.checked==false && mul.checked==false && div.checked==false){
  alert("Select operation")
 }
 
 else{
 if(y!=0){
  document.getElementById("para").innerHTML=x/y}
 else{
  alert("Division by zero")
   }
 }
}

function clearres(){
 document.getElementById("add").checked=false
 document.getElementById("sub").checked=false
 document.getElementById("mul").checked=false
 document.getElementById("div").checked=false

 document.getElementById("para").innerHTML=""
 
 document.getElementById("num1").value=""
 document.getElementById("num2").value=""
}
