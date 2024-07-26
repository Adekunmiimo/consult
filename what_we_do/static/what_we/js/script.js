

const dropBtn = document.querySelector("#dropdown")
const dropBtn2 = document.querySelector("#dropdown2")
const dropBtn3 = document.querySelector("#dropdown3")
const dropBtn4 = document.querySelector("#dropdown4")
const dropBtn5 = document.querySelector("#dropdown5")

let isDrop = false
let isDrop2 = false
let isDrop3 = false
let isDrop4 = false
let isDrop5 = false
dropBtn.addEventListener("click", ()=>{
    const dropDown = document.querySelector("#dropdownMenu")
    
    isDrop = !isDrop

    isDrop ? dropDown.setAttribute("class", "dropdownMenu") : dropDown.setAttribute("class", "dropdownHide")

})
dropBtn2.addEventListener("click", ()=>{
    const dropDown2 = document.querySelector("#dropdownMenu2")
    
    isDrop2 = !isDrop2

    isDrop2 ? dropDown2.setAttribute("class", "dropdownMenu") : dropDown2.setAttribute("class", "dropdownHide")

})
dropBtn3.addEventListener("click", ()=>{
    const dropDown3= document.querySelector("#dropdownMenu3")
    
    isDrop3 = !isDrop3

    isDrop3 ? dropDown3.setAttribute("class", "dropdownMenu") : dropDown3.setAttribute("class", "dropdownHide")

})
dropBtn4.addEventListener("click", ()=>{
    const dropDown4= document.querySelector("#dropdownMenu4")
    
    isDrop4 = !isDrop4

    isDrop4 ? dropDown4.setAttribute("class", "dropdownMenu") : dropDown4.setAttribute("class", "dropdownHide")

})
dropBtn5.addEventListener("click", ()=>{
    const dropDown5= document.querySelector("#dropdownMenu5")
    
    isDrop5 = !isDrop5

    isDrop5 ? dropDown5.setAttribute("class", "dropdownMenu") : dropDown5.setAttribute("class", "dropdownHide")

})