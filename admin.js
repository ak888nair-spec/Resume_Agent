const API="https://resume-agent-4ifb.onrender.com";

const login=document.getElementById("login");
const panel=document.getElementById("panel");
const message=document.getElementById("message");
const status=document.getElementById("status");

async function refresh(){

    const response=await fetch(API+"/admin/recruit/status");

    const data=await response.json();

    status.innerHTML=data.recruitment
    ?"🟢 Recruitment Open"
    :"🔴 Recruitment Closed";

}

login.onclick=async()=>{

    const password=document.getElementById("password").value;

    const response=await fetch(API+"/admin/login",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            password:password
        })

    });

    if(response.ok){

        panel.style.display="block";

        message.innerHTML="";

        refresh();

    }

    else{

        message.innerHTML="Incorrect Password";

    }

};

document.getElementById("open").onclick=async()=>{

    await fetch(API+"/admin/recruit/open",{

        method:"POST"

    });

    refresh();

};

document.getElementById("close").onclick=async()=>{

    await fetch(API+"/admin/recruit/close",{

        method:"POST"

    });

    refresh();

};