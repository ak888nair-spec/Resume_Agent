const API="https://resume-agent-4ifb.onrender.com";

const login=document.getElementById("login");
const panel=document.getElementById("panel");
const message=document.getElementById("message");
const status=document.getElementById("status");

async function refresh() {
    try {
        const response = await fetch(API + "/admin/recruit/status");

        if (!response.ok) {
            throw new Error("Failed to fetch status");
        }

        const data = await response.json();

        status.innerHTML = data.recruitment
            ? "🟢 Recruitment Open"
            : "🔴 Recruitment Closed";

    } catch (err) {
        console.error(err);
        message.innerHTML = "Unable to fetch recruitment status.";
    }
}

login.onclick = async () => {
    try {
        const password = document.getElementById("password").value;

        const response = await fetch(API + "/admin/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                password: password
            })
        });

        if (!response.ok) {
            message.innerHTML = "Incorrect Password";
            return;
        }

        panel.style.display = "block";
        message.innerHTML = "";

        await refresh();

    } catch (err) {
        console.error(err);
        message.innerHTML = "Server connection failed.";
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