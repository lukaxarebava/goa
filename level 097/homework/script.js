const result = document.getElementById("result")

const display = (btnValue) => {
    result.value += btnValue
}

const clearDisplay = () => {
    result.value = ""
}

const calculate = () => {
    try {
        let expression = result.value

        if (expression.includes("^")) {
            expression = expression.replace(/(\d+)\^(\d+)/g, "Math.pow($1,$2)")
        }

        result.value = eval(expression)
    } catch {
        result.value = "Error"
    }
}

const evenOdd = () => {
    let numbersOnly = result.value.replace(/[^0-9]/g, "")

    if (numbersOnly === "") {
        result.value = "No Numbers Found!"
        return
    }

    let num = parseInt(numbersOnly)

    if (num % 2 === 0) {
        result.value = `${num} is Even`
    } else {
        result.value = `${num} is Odd`
    }
}
