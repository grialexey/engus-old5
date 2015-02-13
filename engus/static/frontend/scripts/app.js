$(document).ready(function() {
    var cardList = new CardList($('.card-list'));
    new CardCreatorQuick($('.card__form--create-top'), $('.header__menu-link--add'), $('.content__overlay'));
    new CardCreatorForArticle($('.card__form--create-article'));
});