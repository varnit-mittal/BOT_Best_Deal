from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    x_currency=input("Enter Currency: ")
    # "USD"
    bot.change_currency(currency=x_currency)
    place=input("Enter Visiting Place: ")
    # 'New York'
    bot.select_place_to_go(place)
    #aria-label="16 April 2023"
    check_in_date=input("Enter Your Check-In Date: ")
    check_out_date=input("Enter Your Check-Out Date: ")
    # "16 April 2023"
    bot.select_dates(check_in_date,check_out_date)
    count=int(input("Enter No. Of Adults Visiting: "))
    bot.select_adults(count)
    bot.click_search()
    bot.apply_filtration()
    bot.driver.refresh()
    bot.report_results()