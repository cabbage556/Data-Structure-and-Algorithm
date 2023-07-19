function gameWinner(numberOfCoins, currentPlayer = "you") {
    if (numberOfCoins <= 0) {
        return currentPlayer;
    }

    let nextPlayer;

    if (currentPlayer === "you") {
        nextPlayer = "them";
    } else if (currentPlayer === "them") {
        nextPlayer = "you";
    }

    if (
        gameWinner(numberOfCoins - 1, nextPlayer) === currentPlayer ||
        gameWinner(numberOfCoins - 2, nextPlayer) === currentPlayer
    ) {
        return currentPlayer;
    } else {
        return nextPlayer;
    }
}

function gameWinner2(numberOfCoins) {
    if ((numberOfCoins - 1) % 3 === 0) {
        return "them";
    } else {
        return "you";
    }
}

console.log(gameWinner2(4));
