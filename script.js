const API="https://resume-agent-4ifb.onrender.com";

const uploadButton=document.getElementById("uploadButton");

const status=document.getElementById("status");

const result=document.getElementById("result");

const resume=document.getElementById("resume");

async function updateStatus(){

const response=await fetch(API+"/admin/recruit/status");

const data=await response.json();

if(data.recruitment){

status.innerHTML="🟢 Recruitment Open";

uploadButton.disabled=false;

}

else{

status.innerHTML="🔴 Recruitment Closed";

uploadButton.disabled=true;

}

}

updateStatus();

uploadButton.onclick=async()=>{

if(resume.files.length===0){

alert("Choose a Resume");

return;

}

const formData=new FormData();

formData.append("file",resume.files[0]);

result.innerHTML="Uploading...";

const response=await fetch(API+"/upload/",{

method:"POST",

body:formData

});

const data=await response.json();

if(response.ok){

result.innerHTML="✅ Resume Processed Successfully";

}

else{

result.innerHTML=data.detail;

}

};