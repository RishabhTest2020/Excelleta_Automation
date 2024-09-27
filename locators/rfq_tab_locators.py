from selenium.webdriver.common.by import By

add_rfq_btn = (By.XPATH, '//button[contains(text(), "Add New RFQ")]')
customer_info_txt = (By.XPATH, '//h3[contains(text(), "Customer Information")]')
rfq_heading = (By.XPATH, '//h3[contains(text(), "heading")]')
rfq_acc_name = (By.XPATH, '//input[contains(@placeholder,"Search Account")]')
rfq_key_contact_person = (By.XPATH, '//input[contains(@placeholder, "Search Key Contact Person")]')
select_key_contact_peroson = (By.XPATH, '(//input[contains(@placeholder, "Search Key Contact Person")]/..//li)[1]')
business_info_txt = (By.XPATH, '//h3[contains(text(), "Business Information")]')
rfq_business_evaluation = (By.XPATH, '//*[@id="businessEvaluationId"]')
rfq_business_evaluation_options = (By.XPATH, '(//select[@id= "businessEvaluationId"]/option)')
rfq_business_domain = (By.XPATH, '(//select[@id= "businessDomainId"]/option)[2]')
rfq_business_nature = (By.XPATH, '//select[@id="businessNatureId"]')
rfq_business_nature_select = (By.XPATH, '(//select[@id="businessNatureId"]/option)[2]')
rfq_business_segment = (By.XPATH, '//select[@formcontrolname="businessSegmentId"]')
rfq_business_segment_select = (By.XPATH, '(//select[@formcontrolname="businessSegmentId"]/option)[2]')
rfq_business_value = (By.XPATH, '//select[@formcontrolname="businessValueId"]')
rfq_business_value_select = (By.XPATH, '(//select[@formcontrolname="businessValueId"]/option)')
rfq_confidentiality = (By.XPATH, '//select[@formcontrolname="confidentialityId"]')
rfq_confidentiality_select = (By.XPATH, '(//select[@formcontrolname="confidentialityId"]/option)')
rfq_received_date_loc = (By.XPATH, '//*[@for="rfqReceivedDate"]/..//input')
rfq_target_date_loc = (By.XPATH, '//*[contains(text(), "Customer Target Date")]/..//input')
rfq_dev_lead_loc = (By.XPATH, '//select[@formcontrolname="developmentLeadLocId"]')
rfq_dev_lead_loc_select_opts = (By.XPATH, '(//select[@formcontrolname="developmentLeadLocId"]/option)')
rfq_dev_lead_loc_select = (By.XPATH,
                           '(//select[@formcontrolname="developmentLeadLocId"]/option[contains(text(), "devleadlocaton")])')
rfq_manufacturing_loc = (By.XPATH, '//select[@formcontrolname="manufacturingLocId"]')
rfq_manufacturing_loc_select_opts = (By.XPATH, '(//select[@formcontrolname="manufacturingLocId"]/option)')
rfq_manufacturing_loc_select = (By.XPATH,
                                '(//select[@formcontrolname="manufacturingLocId"]/option[contains(text(), "manulocation")])')
rfq_company_priority_loc = (By.XPATH, '//select[@formcontrolname="companyPriorityId"]')
rfq_company_priority_loc_select = (By.XPATH, '(//select[@formcontrolname="companyPriorityId"]/option)')

project_details_txt = (By.XPATH, '//h3[contains(text(), "Project Details")]')
rfq_generate_quote_loc = (By.XPATH, '//select[@formcontrolname="generateQuotationById"]')
rfq_generate_quote_loc_select = (By.XPATH, '(//select[@formcontrolname="generateQuotationById"]/option)[2]')
annum_vol_txtbox = (By.XPATH, '//input[@formcontrolname="perAnnumVolumeReq"]')
rfq_annum_vol_loc = (By.XPATH, '//select[@formcontrolname="volumeUnitId"]')
rfq_annum_vol_loc_select = (By.XPATH, '(//select[@formcontrolname="volumeUnitId"]/option)')
day_vol_txtbox = (By.XPATH, '//input[@formcontrolname="perDayVolumeReq"]')
rfq_day_vol_loc = (By.XPATH, '//select[@formcontrolname="dayVolumeUnitId"]')
project_life_txtbox = (By.XPATH, '//input[@formcontrolname="projectLife"]')
rfq_project_life_loc = (By.XPATH, '//select[@formcontrolname="projectLifeId"]')
rfq_project_life_select = (By.XPATH, '(//select[@formcontrolname="projectLifeId"]/option)')
rfq_estimates_sop_loc = (By.XPATH, '//*[contains(text(), "Estimates SOP")]/..//input')
sample_quantity_txt = (By.XPATH, '//h3[contains(text(), "Sample Quantity")]')

timeline_txt = (By.XPATH, '//h3[contains(text(), "Timeline")]')
finalize_date_loc = (By.XPATH, '//*[contains(text(), "TE Finalizing Date")]/..//input')
cft_review_loc = (By.XPATH, '//*[contains(text(), "CFT Review")]/..//input')
costing_completed_loc = (By.XPATH, '//*[contains(text(), "Costing Completed")]/..//input')
rfq_offer_validity_loc = (By.XPATH, '//select[@formcontrolname="offerValidity"]')
rfq_offer_validity_select = (By.XPATH, '(//select[@formcontrolname="offerValidity"]/option)')

costing_txt = (By.XPATH, '//h3[contains(text(), "Costing")]')
costing_format_loc = (By.XPATH, '//select[@formcontrolname="costingFormatId"]')
costing_format_select = (By.XPATH, '(//select[@formcontrolname="costingFormatId"]/option)')
currency_loc = (By.XPATH, '//select[@formcontrolname="currencyId"]')
currency_select = (By.XPATH, '(//select[@formcontrolname="currencyId"]/option)')
packing_cost_loc = (By.XPATH, '//select[@formcontrolname="packagingCostId"]')
packing_cost_select = (By.XPATH, '(//select[@formcontrolname="packagingCostId"]/option)')

logistics_txt = (By.XPATH, '//h3[contains(text(), "Logistics")]')
incoterms_loc = (By.XPATH, '//select[@formcontrolname="incotermId"]')
incoterms_select = (By.XPATH, '(//select[@formcontrolname="incotermId"]/option)')
rfq_shipping = (By.XPATH, '//select[@formcontrolname="accShippingId"]')
rfq_shipping_select = (By.XPATH, '(//select[@formcontrolname="accShippingId"]/option)[2]')
rfq_add_new_addr_btn = (By.XPATH, '//button[contains(text(), "Add New Address")]')

other_info_txt = (By.XPATH, '//h3[contains(text(), "Other Information")]')
roi_chkbox = (By.XPATH, '//input[@formcontrolname="roiEvalution"]')
tect_feas_chkbox = (By.XPATH, '//input[@formcontrolname="techFeasibility"]')
satc_chkbox = (By.XPATH, '//input[@formcontrolname="sendAttachmentToCustomer"]')
compound_feas_chkbox = (By.XPATH, '//input[@formcontrolname="compoundFeasibility"]')

manager_det_txt = (By.XPATH, '//h3[contains(text(), "Manager Details")]')
pm_lead_loc = (By.XPATH, '//select[@formcontrolname="ProjectManagerLead"]')
pm_lead_select = (By.XPATH, '(//select[@formcontrolname="ProjectManagerLead"]/option)[2]')
mk_lead_loc = (By.XPATH, '//select[@formcontrolname="MarketingLead"]')
mk_lead_select = (By.XPATH, '(//select[@formcontrolname="MarketingLead"]/option)[2]')
dev_lead_loc = (By.XPATH, '//select[@formcontrolname="DevelopmentLead"]')
dev_lead_select = (By.XPATH, '(//select[@formcontrolname="DevelopmentLead"]/option)[2]')
surface_treat_loc = (By.XPATH, '//select[@formcontrolname="SurfaceTreatmentHead"]')
surface_treat_select = (By.XPATH, '(//select[@formcontrolname="SurfaceTreatmentHead"]/option)[2]')
plant_head_loc = (By.XPATH, '//select[@formcontrolname="PlantHead"]')
plant_head_select = (By.XPATH, '(//select[@formcontrolname="PlantHead"]/option)[2]')
cft_member_loc = (By.XPATH, '//select[@formcontrolname="ManagementCFTMember"]')
cft_member_select = (By.XPATH, '(//select[@formcontrolname="ManagementCFTMember"]/option)[2]')
dev_head_loc = (By.XPATH, '//select[@formcontrolname="BusinessDevelopmentHead"]')
dev_head_select = (By.XPATH, '(//select[@formcontrolname="BusinessDevelopmentHead"]/option)[2]')

text_boxes = {'annual_amount_txtbox': ('xpath', '//input[@formcontrolname="annualBusinessAmount"]'),
              'project_details_txtbox': ('xpath', '//input[@formcontrolname="projectDetail"]'),
              'model_name_txtbox': ('xpath', '//input[@formcontrolname="modelName"]'), 'assembly_name_txtbox':
                  ('xpath', '//input[@formcontrolname="assemblyName"]'), 'assembly_no_txtbox':
                  ('xpath', '//input[@formcontrolname="assemblyNumber"]'), 'currency_base_txtbox':
                  ('xpath', '//input[@formcontrolname="currencyBaseRateVal"]'), 'target_cost_txtbox':
                  ('xpath', '//input[@formcontrolname="targetCostOfCustomer"]'), 'port_delivery_txtbox':
                  ('xpath', '//input[@formcontrolname="nearestDeliveryPort"]')}

rfq_toggles_loc = {
    'rfq_external_testing': (By.XPATH, '(//*[contains(text(), "External Testing")]/..//input)[2]'),
    'rfq_standard_available': (By.XPATH, '(//*[contains(text(), "Standards Available")]/..//input)[2]'),
    'rfq_sample_quantity': (By.XPATH, '(//*[contains(text(), "Sample Required")]/..//input)[2]'),
    'norms_settled': (By.XPATH, '(//*[contains(text(), "Norms Settled")]/..//input)[2]'),
    'tooling_cost': (By.XPATH, '(//*[contains(text(), "Tooling Cost")]/..//input)[2]'),
}

rfq_surface_treatment_loc = (By.XPATH, '(//*[contains(text(), "Surface Treatment Required")]/..//input)[1]')
assembly_type_tog_loc = (By.XPATH, '(//*[contains(text(), "Assembly Type")]/..//input)[2]')

diagram_highlight_blink = (By.XPATH, '//h4[contains(text(), "Stage")]/..//div[@class = "act-border"]')
add_drawing_diagram = (By.XPATH, '//button[contains(text(), "Add Drawing Data")]')
drawing_fields_locs = [(By.XPATH, '//input[@formcontrolname="drawingName"]'),
                       (By.XPATH, '//input[@formcontrolname="customerDrwOrDocNO"]'),
                       (By.XPATH, '//textarea[@formcontrolname="remarks"]')]
twod_soft_copy = (By.XPATH, '//select[@formcontrolname="twoDCopy"]')
twod_soft_copy_select = (By.XPATH, '(//select[@formcontrolname="twoDCopy"]/option)')
threed_soft_copy = (By.XPATH, '//select[@formcontrolname="threeDCopy"]')
threed_soft_copy_select = (By.XPATH, '(//select[@formcontrolname="threeDCopy"]/option)')
upload_soft_copy = (By.XPATH, '(//span[@class="upload-soft-copy"]/input)')
copy_received_date = (By.XPATH, '(//input[@placeholder="select Date"])')

add_roi_btn = (By.XPATH, '//button[contains(text(), "Add ROI")]')
roi_field_loc = (By.XPATH, '//input[@id="ROI-year"]')
roi_file_loc = (By.XPATH, '//input[@id="roiFile"]')
save_btn = (By.XPATH, '//button[contains(@type, "submit")]')
roi_menu_btn = (By.XPATH, '//div[@id="rfq-data3"]//button')
approve_roi_te = (By.XPATH, '//*[contains(@class, "menuAction")]//*[contains(text(), "Approve")]')
reject_roi_te = (By.XPATH, '//*[contains(@class,"menu-list")]//*[contains(text(),"Reject")]')
revoke_roi_te = (By.XPATH, '//*[contains(@class,"menu-list")]//*[contains(text(),"Revoke")]')
add_comment = (By.XPATH, '//input[@id="comment"]')

add_technical_feasibility = (By.XPATH, '//button[contains(text(), "Add Technical Feasibility")]')
tech_feasi_is_no_loc = (By.XPATH, '//label[contains(@class,"radio-label") and span[text()="No"]]')
tf_file_loc = (By.XPATH, '//input[@id="feasibilitySheet"]')
te_menu_btn = (By.XPATH, '//div[@id="rfq-data4"]//*[contains(@class,"menuAction")]//button')

te_name_link = (By.XPATH, '//div[@class="rfqSection"]//td[@class="link"]')

rfq_table_row_loc = (By.XPATH, '(//a[contains(text(), "acc_name")]/../../..//*[contains(@class, "ag-cell-value")]/span)')

rfq_more_details_btn_loc = (By.XPATH, '//*[contains(@class,"companyDetails")]//*[contains(text(),"RFQ More Details")]')
rfq_details_edit_btn_loc = (By.XPATH, '//*[contains(@class,"action-btns")]//*[contains(@alt,"edit_icon")]')
manager_details_header_loc = (By.XPATH, '//*[contains(@formgroupname,"managerDetails")]//h3[contains(text(),"Manager Details")]')

compound_feas_as_yes_loc = (By.XPATH, '//label[contains(@class,"radio-label") and span[text()="Yes"]]')
add_compound_feasibility_loc = (By.XPATH, '//*[contains(text(),"Add Compound Feasibility")]')
compound_cf_sheet_input_loc = (By.XPATH, '//input[@id="compoundFeasibilitySheet"]')
