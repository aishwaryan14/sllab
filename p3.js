function submit(){
 var x=document.getElementById("word").value
 maxlen=0;
 longest_wrd="";
 w=x.split(" ");
 for(i=0;i<w.length;i++){
	if(maxlen<w[i].length)
            maxlen = w[i].length
	    longest_wrd=w[i];		
	}
     document.getElementById("para").innerHTML=maxlen;
}
