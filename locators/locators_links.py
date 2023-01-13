from selenium.webdriver.common.by import By

# Links titles and locators

MAIN_MENU_TITLES = {
    "Video Templates | 3000+ Creative Online Video Ad Templates": (By.XPATH, '//*[@data-qaid="templates"]'),
    "Pricing & Plans | Promo.com | Marketing Video Maker": (By.XPATH, '//*[@data-qaid="header_link_pricing"]'),
    "FAQ | Promo.com | Marketing Video Maker": (By.XPATH, '//*[@data-qaid="header_submenu_faq"]')
}
# RESOURCES_HEADER = (By.XPATH, '//SPAN[@data-qaid="header_resources"]')
RESOURCES_HEADER = (By.XPATH, '//A[text()="Resources "]')
MAIN_MENU_TAB_TITLES = {
    # 'Social Media Calendar: Videos for Every Day of the Month | Promo.com':
    #     (By.XPATH, "//a[@data-qaid='header_link_calendar']"),
    'Blog - Promo.com':
        (By.XPATH, "//a[@data-qaid='header_submenu_blog']"),
}

FOOTER_MENU_TITLES = {
    'Pricing & Plans | Promo.com | Marketing Video Maker': (By.XPATH, "//A[@data-qaid='footer_pricing']"),
    'About Us | Promo.com | Marketing Video Maker': (By.XPATH, "//A[@data-qaid='footer_about']"),
    'Promo.com Newsroom - Promo.com': (By.XPATH, "//A[@data-qaid='footer_news']"),
    'Promo.com Affiliates Program | Promo.com': (By.XPATH, "//A[@data-qaid='footer_affiliates']"),
    'FAQ | Promo.com | Marketing Video Maker': (By.XPATH, "//A[@data-qaid='footer_faq']"),
    'Promo.com Knowledge Base': (By.XPATH, "//A[@data-qaid='footer_knowledge_base']"),
    'Terms of Service | Promo.com | Visual Content Creation Platform':
        (By.XPATH, "//A[@data-qaid='footer_tos']"),
    'Privacy Policy | Promo.com | Visual Content Creation Platform':
        (By.XPATH, "//A[@data-qaid='footer_privacy_policy']"),
    'Cookies Policy | Promo.com | Visual Content Creation Platform':
        (By.XPATH, "//A[@data-qaid='footer_cookies_policy']")
}

FOOTER_PRODUCT_TITLES = {
    'Careers - Promo.com': (By.XPATH, '//*[@data-qaid="footer_careers"]'),
    'Write For Us - Promo.com': (By.XPATH, "//A[@data-qaid='footer_write_for_us']"),
    #'Blog - Promo': (By.XPATH, "//A[@data-qaid='footer_blog']"),
    'Promo Video Maker | Create Quick Promotional Videos Online': (By.XPATH, "//A[@data-qaid='footer_for_promo']"),
    'Commercial Maker - How to Make a Commercial l Promo.com': (By.XPATH, "//A[@data-qaid='footer_for_commercial']"),
    'Social Media Video Maker | Create Videos for Social Media': (By.XPATH, "//A[@data-qaid='footer_for_social']"),
    'eCommerce Ads | Create eCommerce Videos Easily | Promo.com': (By.XPATH, "//A[@data-qaid='footer_for_ecommerce']"),
    'Facebook Video Maker | Create Facebook Videos in Minutes!':
        (By.XPATH, "//A[@data-qaid='footer_for_fb_video_maker']"),
    'Facebook Video Ad Creator | Make Catchy Facebook Ads':
        (By.XPATH, "//A[@data-qaid='footer_for_fb_video_ad_creator']"),
    'Facebook Story Ads | Facebook Story Video Ad Creator':
        (By.XPATH, "//A[@data-qaid='footer_for_fb_story_ads']"),
    'Instagram Video Maker | Promo.com':
        (By.XPATH, "//A[@data-qaid='footer_for_ig_video_maker']"),
    'Instagram Ad Maker | Promo.com':
        (By.XPATH, "//A[@data-qaid='footer_for_ig_video_ad_maker']"),
    'Instagram Story Ads | Create Instagram Story Ads Easily | Promo.com':
        (By.XPATH, "//A[@data-qaid='footer_for_ig_story_ads']"),
    'YouTube Video Maker | Create Many YouTube Videos & Clips':
        (By.XPATH, "//A[@data-qaid='footer_for_yt_video_maker']"),
    'YouTube Ad Maker | Create YouTube Video Ads in minutes!': (By.XPATH, "//A[@data-qaid='footer_for_yt_ad_maker']"),
    'Easy YouTube Intro Creator | Dozens of Templates | Promo.com':
        (By.XPATH, "//A[@data-qaid='footer_for_yt_intro_maker']"),
    'YouTube Outro Maker | Create Outro Videos for YouTube': (By.XPATH, "//A[@data-qaid='footer_for_yt_outro_maker']"),
    'LinkedIn Video Ad Maker | Create LinkedIn Ads Easily | Promo.com':
        (By.XPATH, "//A[@data-qaid='footer_for_li_video_ads']"),
    'Twitter Video Ad Maker | Create Twitter Ads Easily | Promo.com':
        (By.XPATH, "//A[@data-qaid='footer_for_tw_video_ads']"),
    'Amazon Video Ads | Create Amazon Sponsored Ads Easily | Promo.com':
        (By.XPATH, "//A[@data-qaid='footer_for_amazon_video_ads']"),
    'Real Estate Video Maker | Marketing Video Ads for Realtors':
        (By.XPATH, "//A[@data-qaid='footer_for_real_estate_videos']"),
    'Health and Fitness Video Marketing | Create health Ads Today!':
        (By.XPATH, "//A[@data-qaid='footer_for_fitness_marketing_videos']"),
    'Fashion Video Ads Maker | Fashion Marketing and Promotion':
        (By.XPATH, "//A[@data-qaid='footer_for_fashion_marketing_videos']"),
    'Restaurant Marketing Videos | Make Promo Ads for Restaurants':
        (By.XPATH, "//A[@data-qaid='footer_for_restaurant_videos']"),
    'Hair Salon Video and Promo Ideas | Cosmetic Marketing Ads':
        (By.XPATH, "//A[@data-qaid='footer_for_beauty_marketing_videos']"),
    'Travel Video Maker | Travel Agency & Hotel Promo Video Ads': (By.XPATH, "//A[@data-qaid='footer_for_travel_ads']"),
    'Business Video Maker | Promotional Videos for Small Business': (By.XPATH, "//A[@data-qaid='footer_for_business']"),
    #'Human Resources Videos | Hiring & Recruiting | Promo.com': (By.XPATH, "//A[@data-qaid='footer_for_hr']"),
    'Create inspiring videos for NPOs with a free plan | Promo.com':
        (By.XPATH, "//A[@data-qaid='footer_for_nonprofit']"),
}

# Tools - footer
TOOLS_FOOTER_TITLES = {
    'Photos to Video Maker | Create Dynamic Videos in Seconds |Promo.com': (By.XPATH, '//*[@data-qaid="footer_tool_photos_to_video"]'),
    'Video Maker | Create a Video in Minutes | Promo.com': (By.XPATH, "//A[@data-qaid='footer_tool_video_maker']"),
    'Ad Maker: Free Video Ads | Promo.com': (By.XPATH, "//A[@data-qaid='footer_tool_ad_maker']"),
    # 'Social Media Calendar: Videos for Every Day of the Month | Promo.com' or None: (By.XPATH, "//A[@data-qaid='footer_tool_calendar']"),
    'Free Image Resizer | Resize Your Images Online | Promo.com': (By.XPATH, "//A[@data-qaid='footer_tool_resizer']"),
    'Free Online Collage Maker | Collage Templates | Promo.com': (By.XPATH, "//A[@data-qaid='footer_tool_collage']"),
    'Free Facebook Video Covers | Promo | Marketing Video Maker': (By.XPATH, "//A[@data-qaid='footer_tool_fb_covers']"),
    'Video Production Cost Estimator | Promo.com': (By.XPATH, "//A[@data-qaid='footer_tool_video_production']"),
    'Facebook Ad Budget Calculator | Promo.com. | Find out how much to spend': (By.XPATH, "//A[@data-qaid='footer_tool_fb_ad_budget']"),
    'Facebook Ads Troubleshooter for Your Ad Campaigns | Promo.com': (By.XPATH, "//A[@data-qaid='footer_tool_fb_ads_trouble']"),
    'YouTube Money Calculator | Promo.com': (By.XPATH, "//A[@data-qaid='footer_tool_yt_calc']")
}

# Partners logos
PARTNERS_LOGOS = {
    'FB': (By.XPATH, "//img[@alt='meta icon']"),
    'IG': (By.XPATH, "//img[@alt='instagram icon']"),
    'YT': (By.XPATH, "//img[@alt='youtube icon']"),
    'GETTY': (By.XPATH, "//img[@alt='getty icon']"),
    'B2B': (By.XPATH, "//i[@class='ph-icon external-link external-link']//a"),
    'TSM': (By.XPATH, "//section[@class='partners']//i[@class='tsm-icon']//a")
}

TOOLS_TEMPLATES_FOOTER_TITLES = (By.XPATH, '//SPAN[@class="footer-section__title"][text()="Tools"]')
