# CSS

dashboard = ".oxd-main-menu-item"
search = ".oxd-input--active"
left_toggle = ".bi-chevron-left"
widget = ".orangehrm-dashboard-widget"  # Только в xpath через текст могу показать
button_upgrade = ".orangehrm-upgrade-button"
image_profile = ".oxd-userdropdown-img"
widget_setting = ".orangehrm-leave-card-icon"
dashboard_chart = ".oxd-chart-legend .oxd-text.oxd-text--span[title='Engineering']"


# XPath

search_ = "//input[@placeholder='Search']"
dashboard_ = "//*[contains(@class, 'oxd-main-menu-item') and contains(@class, 'active')]"
widget_settings_ = "//i[contains(@class, 'bi-gear-fill')]"
left_toggle_ = "//*[contains(@class, 'bi-chevron-left')]"
button_upgrade_ = "//button[contains(@class, 'orangehrm-upgrade-button')]"
image_profile_ = "//*[@class='oxd-userdropdown-img']"
title_ = "//span[@title='Engineering']"
widget_ = "//div[contains(@class, 'orangehrm-dashboard-widget')][.//p[text()='My Actions']]"
