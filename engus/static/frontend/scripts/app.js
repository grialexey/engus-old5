$(document).ready(function() {
    var cardList = new CardList($('.card-list'));
    new CardCreator($('.card__form--create'), $('.header__menu-link--add'), $('.content__overlay'), cardList);
});