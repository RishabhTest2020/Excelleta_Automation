from helpers.generator import *

accounts_table_header_col = ['Action', 'Account No', 'Account Name', 'Website', 'Email ID', 'Phone Number',
                             'Landline Number', 'Customer Code', 'Business Nature',
                             'Business Domain', 'Payment Method', 'Payment Term', 'Business Segment', 'Address',
                             'Postal Code', 'GSTIN', 'Country', 'State', 'City', 'Created On', 'Last Modified On',
                             'Status']

accounts_create_fields_gen = ['accountName', 'accountEmail', 'website', 'mobileNumber',
                              'landlineNumber', 'panNo', 'customerCode', 'noOfWorkingDays']

accounts_general_details = [random_correct_name(5, 4), f'{random_email_generator()}', 'www.testwesite.com',
                            '9090909090', '12345678', 'QWERT1234Y', f'{generate_random_five_digit_number()}', 7]

start_months_data = ['Select Month', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                     'September', 'October', 'November', 'December']

rm_type_list = ['Select Norms Rate Type', 'Base Rate', 'Landed Rate']

business_nature_list = ['Select All', 'Fabrication', 'Heavy Fabrication']

business_domain_list = ['Select All', 'Domestic', 'Export']

business_segment_list = ['Select All', '2 WHEELER', '3 WHEELER', '4 WHEELER', 'AGRICULTURAL EQUIPMENT',
                         'CONSTRUCTION EQUIPMENT', 'GENSETS/ENGINES', 'RAILWAY', 'TRACTOR', 'WHITE GOODS']

payment_method_list = ['Select Payment Method', 'Cheque', 'NEFT', 'RTGS']

payment_term_list = ['Select Payment Term', 'Advance', '07 days', '15 days', '30 days', '40 days', '45 days',
                     '60 days', '75 days', '90 days', '100 Days']

billing_add_gst_pc_list = ['Test Address, Gurgaon', 210009, '28ABCDE1234F1ZW']

billing_countries_list = ['Select Country', 'Austria', 'Brazil', 'Canada', 'Chile', 'Czech Republic', 'Finland',
                          'France', 'Germany', 'India', 'Italy', 'Netherlands', 'Poland', 'Romania', 'Spain',
                          'Sri Lanka', 'Thailand', 'United Kingdom', 'United States']

billing_india_states_list = ['Select State', 'Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh',
                             'Assam',
                             'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi',
                             'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand',
                             'Karnataka',
                             'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
                             'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                             'Tamil Nadu',
                             'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

billing_uttar_pradesh_cities_list = ['Select City', 'Achhnera', 'Afzalgarh', 'Agra', 'Ahraura', 'Aidalpur', 'Airwa',
                                     'Akbarpur', 'Akola', 'Aliganj', 'Aligarh', 'Allahabad', 'Allahganj'
    , 'Amanpur', 'Amauli', 'Ambahta', 'Ambedkar Nagar', 'Amethi', 'Amroha', 'Anandnagar', 'Antu', 'Anupshahr', 'Aonla',
                                     'Araul', 'Asalatganj', 'Atarra',
                                     'Atrauli', 'Atraulia', 'Auraiya', 'Auras', 'Ayodhya', 'Azamgarh', 'Azizpur',
                                     'Baberu', 'Babina', 'Babrala', 'Babugarh', 'Bachhraon', 'Bachhrawan',
                                     'Baghpat', 'Baghra', 'Bah', 'Baheri', 'Bahjoi', 'Bahraich', 'Bahraigh', 'Bahsuma',
                                     'Bahua', 'Bajna', 'Bakewar', 'Baksar', 'Balamau', 'Baldeo', 'Baldev', 'Ballia',
                                     'Balrampur', 'Banat', 'Banbasa', 'Banda', 'Bangarmau', 'Bansdih', 'Bansgaon',
                                     'Bansi', 'Banthra', 'Bara Banki', 'Baragaon', 'Baraut',
                                     'Bareilly', 'Barhalganj', 'Barkhera', 'Barkhera Kalan', 'Barokhar', 'Barsana',
                                     'Barwar (Lakhimpur Kheri)', 'Basti', 'Behat', 'Bela', 'Belthara', 'Beniganj',
                                     'Beswan', 'Bewar', 'Bhadarsa', 'Bhadohi', 'Bhagwantnagar', 'Bharatpura',
                                     'Bhargain', 'Bharthana', 'Bharwari', 'Bhaupur', 'Bhimtal', 'Bhinga', 'Bhognipur',
                                     'Bhongaon', 'Bidhnu', 'Bidhuna', 'Bighapur', 'Bighapur Khurd', 'Bijnor', 'Bikapur',
                                     'Bilari', 'Bilariaganj', 'Bilaspur', 'Bilgram',
                                     'Bilhaur', 'Bilsanda', 'Bilsi', 'Bilthra', 'Binauli', 'Binaur', 'Bindki',
                                     'Birdpur', 'Birpur', 'Bisalpur', 'Bisanda Buzurg', 'Bisauli', 'Bisenda Buzurg',
                                     'Bishunpur Urf Maharajganj', 'Biswan', 'Bithur', 'Budaun', 'Budhana',
                                     'Bulandshahr', 'Captainganj', 'Chail', 'Chakia', 'Chandauli', 'Chandauli District',
                                     'Chandausi', 'Chandpur', 'Chanduasi', 'Charkhari', 'Charthawal', 'Chhaprauli',
                                     'Chharra', 'Chhata', 'Chhibramau', 'Chhitauni', 'Chhutmalpur', 'Chillupar',
                                     'Chirgaon', 'Chitrakoot', 'Chitrakoot Dham', 'Chopan', 'Chunar', 'Churk',
                                     'Colonelganj', 'Dadri', 'Dalmau', 'Dankaur', 'Daraganj', 'Daranagar', 'Dasna',
                                     'Dataganj', 'Daurala', 'Dayal Bagh', 'Deoband', 'Deogarh', 'Deoranian', 'Deoria',
                                     'Derapur', 'Dewa', 'Dhampur', 'Dhanaura',
                                     'Dhanghata', 'Dharau', 'Dhaurahra', 'Dibai', 'Divrasai', 'Dohrighat',
                                     'Domariaganj', 'Dostpur', 'Dudhi', 'Etah', 'Etawah', 'Etmadpur', 'Faizabad',
                                     'Farah', 'Faridnagar', 'Faridpur', 'Farrukhabad', 'Fatehabad', 'Fatehganj West',
                                     'Fatehgarh', 'Fatehpur', 'Fatehpur (Barabanki)', 'Fatehpur Chaurasi',
                                     'Fatehpur Sikri', 'Firozabad', 'Fyzabad', 'Gahlon', 'Gahmar', 'Gaini', 'Gajraula',
                                     'Gangoh', 'Ganj Dundawara', 'Ganj Dundwara', 'Ganj Muradabad',
                                     'Garautha', 'Garhi Pukhta', 'Garhmuktesar', 'Garhwa', 'Gauriganj',
                                     'Gautam Buddha Nagar', 'Gawan', 'Ghatampur', 'Ghaziabad', 'Ghazipur', 'Ghiror',
                                     'Ghorawal', 'Ghosi', 'Gohand', 'Gokul', 'Gola Bazar', 'Gola Gokarannath', 'Gonda',
                                     'Gopamau', 'Gorakhpur', 'Gosainganj', 'Goshainganj', 'Govardhan',
                                     'Greater Noida', 'Gulaothi', 'Gunnaur', 'Gursahaiganj', 'Gursarai', 'Gyanpur',
                                     'Haldaur', 'Hamirpur', 'Handia', 'Hapur', 'Haraipur', 'Haraiya', 'Harchandpur',
                                     'Hardoi', 'Harduaganj', 'Hasanpur', 'Hastinapur', 'Hata', 'Hata (India)',
                                     'Hathras', 'Hulas', 'Ibrahimpur', 'Iglas', 'Ikauna', 'Indergarh', 'Indragarh',
                                     'Islamnagar', 'Islamnagar (Badaun)', 'Itaunja', 'Itimadpur', 'Jagdishpur',
                                     'Jagnair', 'Jahanabad', 'Jahanabad (Pilibhit)', 'Jahangirabad', 'Jahangirpur',
                                     'Jainpur', 'Jais', 'Jalalabad', 'Jalali', 'Jalalpur', 'Jalaun', 'Jalesar',
                                     'Janghai', 'Jansath', 'Jarwa', 'Jarwal', 'Jasrana'
    , 'Jaswantnagar', 'Jaunpur', 'Jewar', 'Jhajhar', 'Jhalu', 'Jhansi', 'Jhinjhak', 'Jhinjhana', 'Jhusi', 'Jiyanpur',
                                     'Jyotiba Phule Nagar', 'Kabrai', 'Kachhwa', 'Kadaura', 'Kadipur', 'Kagarol',
                                     'Kaimganj', 'Kairana', 'Kakori', 'Kakrala', 'Kalinagar', 'Kalpi', 'Kalyanpur',
                                     'Kamalganj', 'Kampil', 'Kandhla', 'Kannauj', 'Kanpur', 'Kanpur Dehat', 'Kant',
                                     'Kanth', 'Kaptanganj', 'Kara', 'Karari', 'Karbigwan', 'Karchana', 'Karhal',
                                     'Kasganj', 'Katra',
                                     'Kausani', 'Kaushambi District', 'Kemri', 'Khada', 'Khaga', 'Khailar', 'Khair',
                                     'Khairabad', 'Khalilabad', 'Khanpur', 'Kharela', 'Khargupur', 'Kharkhauda',
                                     'Khatauli', 'Khekra', 'Kheri', 'Khudaganj', 'Khurja', 'Khutar', 'Kirakat',
                                     'Kiraoli', 'Kiratpur', 'Kishanpur', 'Kishanpur baral', 'Kishni',
                                     'Kithor', 'Konch', 'Kopaganj', 'Kosi', 'Kota', 'Kotra', 'Kuchesar', 'Kudarkot',
                                     'Kulpahar', 'Kunda', 'Kundarkhi', 'Kundarki', 'Kurara', 'Kurebharsaidkhanpur',
                                     'Kushinagar', 'Kusmara', 'Kuthaund', 'Laharpur', 'Lakhimpur', 'Lakhna', 'Lalganj',
                                     'Lalitpur', 'Lambhua', 'Lar', 'Lawar', 'Lawar Khas',
                                     'Loni', 'Lucknow', 'Lucknow District', 'Machhali Shahar', 'Machhlishahr',
                                     'Madhoganj', 'Madhogarh', 'Maghar', 'Mahaban', 'Maharajganj', 'Mahmudabad'
    , 'Mahoba', 'Maholi', 'Mahrajganj', 'Mahrajganj (Raebareli)', 'Mahroni', 'Mahul', 'Mailani', 'Mainpuri', 'Majhupur',
                                     'Makanpur', 'Malasa', 'Malihabad', 'Mandawar', 'Maniar', 'Manikpur', 'Manjhanpur',
                                     'Mankapur', 'Marahra', 'Mariahu', 'Mataundh', 'Mathura', 'Mau', 'Mau Aima',
                                     'Mau Aimma', 'Maudaha', 'Maurawan', 'Mawana', 'Mawar', 'Meerut', 'Mehdawal',
                                     'Mehnagar', 'Mehndawal', 'Milak', 'Milkipur', 'Miranpur', 'Miranpur Katra',
                                     'Mirganj', 'Mirzapur', 'Misrikh', 'Mohan', 'Mohanpur', 'Moradabad', 'Moth',
                                     'Mubarakpur', 'Mughal Sarai', 'Muhammadabad', 'Mukteshwar', 'Mungra Badshahpur',
                                     'Munsyari', 'Muradabad', 'Muradnagar', 'Mursan', 'Musafir-Khana', 'Musafirkhana',
                                     'Muzaffarnagar', 'Nadigaon', 'Nagina', 'Nagla', 'Nagram', 'Najibabad', 'Nakur',
                                     'Nanauta', 'Nandgaon', 'Nanpara', 'Narauli', 'Naraura', 'Narora', 'Naugama',
                                     'Naurangpur', 'Nautanwa', 'Nawabganj', 'Nawabganj (Barabanki)',
                                     'Nawabganj (Bareilly)', 'Newara', 'Nichlaul', 'Nigoh', 'Nihtaur', 'Niwari',
                                     'Nizamabad', 'Noida', 'Nurpur', 'Obra', 'Orai', 'Oran', 'Pachperwa', 'Padrauna',
                                     'Pahasu', 'Paigaon', 'Pali', 'Palia Kalan', 'Paras Rampur', 'Parichha',
                                     'Parichhatgarh', 'Parshadepur', 'Pathakpura', 'Patiali', 'Patti',
                                     'Pawayan', 'Payagpur', 'Phalauda', 'Phaphamau', 'Phaphund', 'Phariha', 'Pheona',
                                     'Phulpur', 'Pichhaura', 'Pihani', 'Pilibhit', 'Pilkhua', 'Pilkhuwa', 'Pinahat',
                                     'Pipraich', 'Pipri', 'Pratapgarh', 'Prayagraj (Allahabad)', 'Pukhrayan',
                                     'Puranpur', 'Purmafi',
                                     'Purwa', 'Qadirganj', 'Rabupura', 'Radha Kund', 'Radhakund', 'Raebareli',
                                     'Rajapur', 'Ramkola', 'Ramnagar', 'Rampur', 'Rampura', 'Ranipur', 'Ranipur Barsi',
                                     'Rasra', 'Rasulabad', 'Rath',
                                     'Raya', 'Rehar', 'Renukoot', 'Renukut', 'Reoti', 'Reotipur', 'Richha',
                                     'Robertsganj', 'Rudarpur', 'Rudauli', 'Rura', 'Sabalpur', 'Sachendi', 'Sadabad',
                                     'Sadat', 'Safipur', 'Saharanpur', 'Sahaspur', 'Sahaswan', 'Sahawar', 'Sahibabad',
                                     'Sahpau', 'Saidpur', 'Sakhanu', 'Sakit', 'Salempur', 'Salon',
                                     'Sambhal', 'Samthar', 'Sandi', 'Sandila', 'Sant Kabir Nagar',
                                     'Sant Ravi Das Nagar', 'Sarai Akil', 'Sarai Ekdil', 'Sarai Mir', 'Sarauli',
                                     'Sardhana', 'Sarila', 'Sarurpur', 'Sasni', 'Satrikh', 'Saurikh', 'Sector',
                                     'Seohara', 'Shahabad', 'Shahganj', 'Shahi',
                                     'Shahjahanpur', 'Shahpur', 'Shamli', 'Shamsabad', 'Shankargarh', 'Shergarh',
                                     'Sherkot', 'Shibnagar', 'Shikarpur', 'Shikarpur (Bulandshahr)', 'Shikohabad',
                                     'Shishgarh', 'Shivrajpur', 'Shrawasti', 'Siddharthnagar', 'Siddhaur', 'Sidhauli',
                                     'Sidhpura', 'Sikandarabad', 'Sikandarpur', 'Sikandra', 'Sikandra Rao',
                                     'Sikandrabad', 'Sirathu', 'Sirsa', 'Sirsaganj', 'Sirsi', 'Sisauli', 'Siswa Bazar',
                                     'Sitapur', 'Sonbhadra', 'Soron', 'Suar', 'Sultanpur', 'Surianwan', 'Tajpur',
                                     'Talbahat', 'Talgram', 'Tanda', 'Terha', 'Thakurdwara', 'Thana Bhawan', 'Tigri',
                                     'Tikaitnagar', 'Tikri', 'Tilhar', 'Tilsahri', 'Tindwari', 'Titron',
                                     'Tori Fatehpur', 'Tori-Fatehpur', 'Tulsipur', 'Tundla', 'Ugu', 'Ujhani', 'Umri',
                                     'Un', 'Unnao', 'Usawan', 'Usehat', 'Uska', 'Utraula', 'Varanasi', 'Vindhyachal',
                                     'Vrindavan', 'Walterganj', 'Wazirganj', 'Yusufpur', 'Zafarabad', 'Zaidpur',
                                     'Zamania']

#  Contacts Tab --------------------------------------------------------------------------------------
contacts_create_fields_gen = ['firstName', 'lastName', 'email', 'phoneNumber']

contacts_general_details = [random_correct_name(5, 4, 'first_name'), random_correct_name(5, 4, 'last_name'), f'{random_email_generator()}',
                            '9090909090']

titles_data = ['Select Title', 'Mr', 'Mrs']

department_data = ['Select Department', 'Analysing', 'Costing', 'Design', 'Development', 'Marketing', 'Operations',
                   'Purchase', 'R&D', 'Sales']

designation_data = ['Select Designation', 'Analysing Lead', 'Asst. General Manager', 'Asst. Manager', 'CEO', 'CFO',
                    'COO', 'Director', 'Dpty. General Manager', 'Dpty. Manager', 'Executive', 'General Manager',
                    'Manager', 'Officer', 'Plant Head', 'President', 'Purchase Head', 'Sales Manager', 'Sr. Engineer',
                    'Sr. Executive', 'Sr. General Manager', 'Sr. Manager', 'Sr. Officer', 'Vice President']

report_to_data = ['Select Contact Person']

gender_data = ['Select Gender', 'Male', 'Female', 'Rather not to say']

marital_data = ['Select Status', 'Married', 'Single', 'Rather not to say']

billing_contact_list = [f'{random_correct_name(5, 4, 'first_name')}, Gurgaon', generate_random_five_digit_number(10),
                        f'{random_correct_name(5, 4, 'first_name')}, Gurgaon', generate_random_five_digit_number(10)]

contact_table_header_col = ['Action', 'Profile', 'First Name', 'Account Name', 'Phone Number', 'Email ID', 'Department',
                            'Designation', 'Report To', 'Birth Date', 'Country', 'State', 'City', 'Address',
                            'Residential Country', 'Residential State', 'Residential City', 'Residential Address',
                            'Created On', 'Last Modified On', 'Status']


# rfq test data............................................................................

rfq_txtboxes_data = [10000, 'Test Automation', 'Bajaj pulsar 220F', 'Carburetor', 123, 820, 1200, 'Port delivery text' ]

rfq_business_evaluation_data = ['Select Business Evaluation', 'Existing Product Existing Customer',
                                'Existing Product New Customer', 'New Product Existing Customer',
                                'New Product New Customer']

rfq_business_values_data = ['Select Business value', 'High', 'Low', 'Medium']

rfq_confidentiality_dropdown = ['Select Confidentiality', 'No', 'Yes']


rfq_dev_lead_location_data = ['Select Development Lead Location', 'Delhi Corp', 'MAPL B-03 Waluj', 'MAPL B-12 Waluj',
                         'MAPL B-17 Waluj', 'MAPL B-31 Waluj', 'MAPL Hosur', 'MAPL Pithampur', 'MMT Dharuhera',
                         'MMT Pantnagar -I', 'MMT Pantnagar -III']

rfq_manufacturing_location_data = ['Select Manufacturing Location', 'MAPL B-03 Waluj', 'MAPL B-12 Waluj',
                                   'MAPL B-17 Waluj', 'MAPL B-31 Waluj', 'MAPL Hosur', 'MAPL Pithampur',
                                   'MMT Dharuhera', 'MMT Pantnagar -I', 'MMT Pantnagar -III']


rfq_company_priority_dropdown = ['Select Company Priority', 'High', 'Low', 'Medium']

rfq_units_dropdown = ['Select Unit', 'Sets', 'Units']

rfq_project_life_data = ['Select Life', 'DAYS', 'MONTHS', 'WEEKS', 'YEARS']

rfq_offer_validity_data = ['Select Offer Validity', '7 Days', '15 Days', '30 Days', '45 Days', '60 Days', '75 Days',
                           '90 Days']

rfq_costing_format_data = ['Select Costing Format', 'Both', 'Company', 'Customer']

rfq_currency_data = ['Select a currency', 'BRL', 'CAD', 'CLP', 'EUR', 'INR', 'LKR', 'RON', 'THB', 'USD']

rfq_cost_packaging_dropdown = ['Select Packaging Cost', 'Not to be Quoted', 'Others', 'To be Quoted in Part Cost']

rfq_incoterms_data = ['Select Incoterms', 'Carriage and Insurance Paid To (CIP)', 'Cost and Freight (CFR)',
                      'Cost, insurance & freight (CIF)', 'Delivered at Place (DAP)', 'Delivered at Place Unloaded (DPU)',
                      'Delivered at Terminal (DAT)', 'Delivered duty paid (DDP)', 'Ex-Works (EXW)',
                      'Free alongside ship (FAS)', 'Free Carrier (FCA)', 'Free on board (FOB)']

