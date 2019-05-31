class Locators():

    ###############Home Page objects################

    ##xpath for the 'All' dropdown search button
    searchAll_Dropdown_xpath = '//*[@id="searchDropdownBox"]'
    ##xpath to choose Books from the dropdown
    chooseFromDropdown_Books_xpath = '//*[@id="searchDropdownBox"]/option[6]'
    ##xpath to the search text box
    search_textBox_xpath = '//*[@id="twotabsearchtextbox"]'
    ##xpath to the search button
    search_button_xpath = '//*[@id="nav-search"]/form/div[2]/div/input'
    ##Add text in the search box eg. data catalog, ibps etc.
    enter_search_text = "data catalog"

    ###################Search Results Page objects############################

    ##xpath to the list of search items displayed
    selected_search_result_xpath = '//h2//a//span'
    ##Add the index of item that you want to select. Add 0 if you want to select the first item
    select_search_item_number = 0
    ##xpath to the title of the product selected
    title_of_selected_item = '//h1/span'
    ##xpath to the list of authors of the selected book
    authors_xpath = '//*[@id="bylineInfo"]'
    ##xpath to the number of customers who reviewed the product
    number_of_customers_reviewed = '//*[@id="acrCustomerReviewText"]'
    ##xpath to the average customer reviews for the product
    average_customer_review_stars = '//*[@id="reviewsMedley"]/div/div[1]/div[1]/div/div/div[2]/div/span/span/a/span'
    ##xpath to the list of book editions for design #1
    list_of_book_editions_design1 = '//*[@id="mediaTabs_tabSet"]//li[contains(@id,"mediaTab_heading_")]'
    ##xpath to the list of book editions for design #2
    list_of_book_editions_design2 = '//*[@id="tmmSwatches"]/ul/li[contains(@class,"swatchElement")]'