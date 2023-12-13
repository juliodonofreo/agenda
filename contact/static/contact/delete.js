const form = document.querySelector(".delete");

form.addEventListener("submit", (e)=>{
    const resposta = confirm("Tem certeza que quer deletar?");

    if(!resposta){
        e.preventDefault();
    }
})