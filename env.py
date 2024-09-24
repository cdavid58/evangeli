<<<<<<< HEAD
from getpass import getuser
USER_WINDOWS = getuser()

URL_SERVER = "https://evansoft.ddns.net:8484"
#URL_SERVER = "http://127.0.0.1:9797"
#URL_SERVER = "https://apievansoft.pythonanywhere.com"

URL_APPLICATION = "https://evansoft.ddns.net"
#URL_APPLICATION = "http://127.0.0.1:8000"
# URL_APPLICATION = "http://26.246.95.16:80"
#URL_APPLICATION = "https://facturaevansoft.pythonanywhere.com"


# URL_FILES_SERVER = f"C:/Users/{USER_WINDOWS}/Documents/Project/invoice/static/company/"
URL_FILES_SERVER = "/deploy/invoice/static/company/"
# URL_FILES_SERVER = "/home/facturaevansoft/invoice_new_evansoft/static/company/"

# URL_FILES_TEMPLATE = f"C:/Users/{USER_WINDOWS}/Documents/Project/invoice/template"
URL_FILES_TEMPLATE = "/deploy/invoice/template"
# URL_FILES_TEMPLATE = "/home/facturaevansoft/invoice_new_evansoft/template"


#URL_UNIVERSAL
#**************************************************************************************************************************************************************************************************************

URL_IN_USE = URL_SERVER
URL_FILES = URL_FILES_SERVER
URL_FILES_TEMPLATE = URL_FILES_TEMPLATE

#**************************************************************************************************************************************************************************************************************


#AUTHENTICATION 

LOGIN = f"{URL_IN_USE}/user/Login/"
LOGOUT = f"{URL_IN_USE}/user/LogOut/"

#SUPPLIER

LIST_SUPPLIER = f"{URL_IN_USE}/inventory/List_Supplier/"
CREATE_SUPPLIER = f"{URL_IN_USE}/inventory/Create_Supplier/"
DELETE_SUPPLIER = f"{URL_IN_USE}/inventory/Delete_Supplier/"
GET_SUPPLIER = f"{URL_IN_USE}/inventory/Get_Supplier/"
UPDATE_SUPPLIER = f"{URL_IN_USE}/inventory/Update_Supplier/"
GET_LIST_BEST_SELLING_PRODUCT = f"{URL_IN_USE}/inventory/Get_List_Best_Selling_Product/"
GET_ALL_LIST_BEST_SELLING_PRODUCT = f"{URL_IN_USE}/inventory/Get_All_List_Best_Selling_Product/"

#EMPLOYEE

CREATE_EMPLOYEE = f"{URL_IN_USE}/user/Create_Employee/"
GET_EMPLOYEE = f"{URL_IN_USE}/user/Get_Employee/"
DELETE_USER = f"{URL_IN_USE}/user/Delete_User/"
UPDATE_USER = f"{URL_IN_USE}/user/Update_User/"
GET_LIST_EMPLOYEE = f"{URL_IN_USE}/user/Get_List_Employee/"
QUERY_PERMISSIONS = f"{URL_IN_USE}/user/Query_Permissions/"
GET_LIST_EMAIL = f"{URL_IN_USE}/user/Get_List_Email/"

#INVENTORY

GET_LIST_PRODUCTS = f"{URL_IN_USE}/inventory/Get_List_Products/"
CREATE_PRODUCT = f"{URL_IN_USE}/inventory/Create_Product/"
DELETE_PRODUCT = f"{URL_IN_USE}/inventory/Delete_Product/"
GET_PRODUCT = f"{URL_IN_USE}/inventory/Get_Product/"
UPDATE_PRODUCT = f"{URL_IN_USE}/inventory/Update_Product/"
GET_LIST_PRODUCTS_SUPPLIER = f"{URL_IN_USE}/inventory/Get_List_Products_Supplier/"
PRODUCT_RESERVED_USER = f"{URL_IN_USE}/inventory/Product_Reserved_User/"
RETURN_PRODUCTS = f"{URL_IN_USE}/inventory/Return_Products/"
RETURN_PRODUCT_UNIQUE = f"{URL_IN_USE}/inventory/return_product_UNIQUE/"
VALIDATED_QUANTITY = f"{URL_IN_USE}/inventory/Validated_Quantity/"
LIST_BRANCH = f"{URL_IN_USE}/company/List_Branch/"
SAVE_TRANSFER = f"{URL_IN_USE}/transfers/Save_Transfer/"

CREATE_CATEGORY = f"{URL_IN_USE}/inventory/Create_Category/"
CREATE_SUBCATEGORY = f"{URL_IN_USE}/inventory/Create_Subcategory/"
GET_CATEGORY = f"{URL_IN_USE}/inventory/Get_Category/"
GET_SUBCATEGORY = f"{URL_IN_USE}/inventory/Get_SubCategory/"


#SHOPPING

VERIFIED_INVOICE = f"{URL_IN_USE}/shopping/Verified_Invoice/"
CREATE_SHOPPING = f"{URL_IN_USE}/shopping/Create_Shopping/"


#CUSTOMER

GET_LIST_CUSTOMER = f"{URL_IN_USE}/customer/Get_List_Customer/"
GET_CUSTOMER = f"{URL_IN_USE}/customer/Get_Customer/"
UPDATE_CUSTOMER = f"{URL_IN_USE}/customer/Update_Customer/"
CREATE_CUSTOMER = f"{URL_IN_USE}/customer/Create_Customer/"
DELETE_CLIENT = f"{URL_IN_USE}/customer/Delete_Client/"

#INVOICE

GET_LIST_INVOICE = f"{URL_IN_USE}/invoice/Get_List_Invoice/"
ANNULLED_INVOICE = f"{URL_IN_USE}/invoice/Annulled_Invoice/"
GET_INVOICE = f"{URL_IN_USE}/invoice/Get_Invoice/"
CREATE_INVOICE = f"{URL_IN_USE}/invoice/Create_Invoice/"
GET_SELLING_BY_INVOICE = f"{URL_IN_USE}/invoice/Get_Selling_By_Invoice/"
GET_SELLING_BY_DATE = f"{URL_IN_USE}/invoice/Get_Selling_By_Date/"
SEND_INVOICE_DIAN = f"{URL_IN_USE}/invoice/Send_Invoice_DIAN/"
ANNULLED_INVOICE_BY_PRODUCT = f"{URL_IN_USE}/invoice/Annulled_Invoice_By_Product/"
CREATE_PASS_INVOICE = f"{URL_IN_USE}/invoice/Create_Pass_Invoice/"

### THERIOSOFT
# PDF_TO_BASE64 = "https://theriosoft.com/api/pdf_to_base64/"
PDF_TO_BASE64 = "https://104.248.63.144/api/pdf_to_base64/"


#REPORT

REPORT_INVOICES = f"{URL_IN_USE}/report/Report_Invoices/"
REPORT_INVOICE_ANNULLED = f"{URL_IN_USE}/report/Report_Invoice_Annulled/"
CLOSE_THE_BOX_ALL = f"{URL_IN_USE}/report/Close_The_Box_All/"
HISTORY_INVENTORY = f"{URL_IN_USE}/report/History_Inventory/"


#SETTING

GET_TYPE_WORKER = f"{URL_IN_USE}/setting/Get_Type_Worker/"
GET_TYPE_CONTRACT = f"{URL_IN_USE}/setting/Get_Type_Contract/"
GET_TSUB_TYPE_WORKER = f"{URL_IN_USE}/setting/Get_TSub_Type_Worker/"
GET_PAYROLL_TYPE_DOCUMENT_IDENTIFICATION = f"{URL_IN_USE}/setting/Get_Payroll_Type_Document_Identification/"
GET_MUNICIPALITIES = f"{URL_IN_USE}/setting/Get_Municipalities/"
GET_PERMISSION = f"{URL_IN_USE}/setting/Get_Permission/"
GET_TYPE_DOCUMENT_I = f"{URL_IN_USE}/setting/Get_Type_Document_I/"
GET_TYPE_REGIMEN = f"{URL_IN_USE}/setting/Get_Type_Regimen/"
GET_ALL_UNIT_MEASURES = f"{URL_IN_USE}/setting/Get_All_Unit_Measures/"
GET_TYPE_ORGANIZATION = f"{URL_IN_USE}/setting/Get_Type_Organization/"
GET_RESOLUTION = f"{URL_IN_USE}/company/Get_Resolution/"
GET_BRANCH = f"{URL_IN_USE}/company/Get_Branch/"
GET_RESOLUTION_LIST = f"{URL_IN_USE}/company/Get_Resolution_List/"
UPDATE_RESOLUTION_DIAN = f"{URL_IN_USE}/company/Update_Resolution_DIAN/"
UPDATE_BRANCH = f"{URL_IN_USE}/company/Update_Branch/"
UPDATE_LOGO = f"{URL_IN_USE}/company/Update_Logo/"


#EMAIL

GET_LIST_EMAILS = f"{URL_IN_USE}/emails/Get_List_Emails/"
GET_LIST_EMAIL_SENDER = f"{URL_IN_USE}/emails/Get_List_Email_Sender/"
CREATE_EMAIL = f"{URL_IN_USE}/emails/Create_Email/"
GET_EMAIL = f"{URL_IN_USE}/emails/Get_Email/"
MARK_AS_READ = f"{URL_IN_USE}/emails/Mark_As_Read/"


#PAYROLL

GET_ALL_PAYROLL_EMPLOYEE = f"{URL_IN_USE}/payroll/Get_All_Payroll_Employee/"
BASIC_PAYROLL = f"{URL_IN_USE}/payroll/Basic_Payroll/"
DELETE_PAYROLL = f"{URL_IN_USE}/payroll/Delete_Payroll/"

#WALLET
GET_PASS_INVOICE = f"{URL_IN_USE}/wallet/Get_Pass_Invoice/"
GET_ALL_HISTORY_PASS_INVOICE = f"{URL_IN_USE}/wallet/Get_All_History_Pass_Invoice/"
GET_ALL_HISTORY_PASS_CUSTOMER = f"{URL_IN_USE}/wallet/Get_All_History_Pass_Customer/"



HTML_MENU = """
<div class="collapse navbar-collapse menu_mio" id="navbarVerticalCollapse">
<div class="navbar-vertical-content scrollbar">
  <ul class="navbar-nav flex-column mb-3" id="navbarVerticalNav">
    <li class="nav-item">
         
        {% if request.session.permission %}
            {% for i in request.session.permission %}
                {% if i == "Facturacion"  or i == "Todos" %}
                    <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
                        <div class="col-auto navbar-vertical-label">Operaciones</div>
                        <div class="col ps-0">
                          <hr class="mb-0 navbar-vertical-divider" />
                        </div>
                    </div>
                    <a class="nav-link dropdown-indicator" href="#events" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="events">
                        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="far fa-file-alt"></span></span><span class="nav-link-text ps-1">Crear Documentos</span>
                        </div>
                    </a>
                    <ul class="nav collapse false" id="events">
                        <li class="nav-item"><a class="nav-link" href="{% url 'Create_Invoice' %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura</span>
                            </div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Documento Soporte </span>
                            </div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Crédito</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Debito</span></div>
                          </a>
                        </li>
                    </ul>
                    <a class="nav-link dropdown-indicator" href="#document" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="document">
                        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="far fa-file-alt"></span></span><span class="nav-link-text ps-1">Documentos Generados</span>
                        </div>
                    </a>
                    <ul class="nav collapse false" id="document">
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 1 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura POS</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 2 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura Electrónica</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 3 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Crédito</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 4 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Debito</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 5 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Documento Soporte </span></div>
                          </a>
                        </li>                            
                    </ul>
                {% endif %}
            {% endfor %}
        {% endif %}
    </li>
    <li class="nav-item">
        
        <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
            <div class="col-auto navbar-vertical-label">Administración</div>
            <div class="col ps-0">
              <hr class="mb-0 navbar-vertical-divider" />
            </div>
        </div>
        {% if request.session.permission %}
            {% for i in request.session.permission %}
                {% if i != "Contador" %}
                    <a class="nav-link" href="{% url 'Get_List_Customer' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-users"></span>
                            </span>
                            <span class="nav-link-text ps-1">Clientes</span>
                        </div>
                    </a>
                {% endif %}
            {% endfor %}
        {% endif %}
        {% if request.session.permission %}
            {% for i in request.session.permission %}
                {% if i == "Administrativo" or i == "Todos" or i == 'Creador' %}
                    <a class="nav-link" href="{% url 'Register_Purchase' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-shopping-cart"></span>
                            </span>
                            <span class="nav-link-text ps-1">Compras</span>
                        </div>
                    </a>
                    <a class="nav-link" href="{% url 'List_Supplier' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-users"></span>
                            </span>
                            <span class="nav-link-text ps-1">Proveedores</span>
                        </div>
                    </a>
                    <a class="nav-link" href="{% url 'Get_List_Products' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-archive"></span>
                            </span>
                            <span class="nav-link-text ps-1">Inventario</span>
                        </div>
                    </a>
                    <a class="nav-link" href="{% url 'Transfer' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-archive"></span>
                            </span>
                            <span class="nav-link-text ps-1">Traslados</span>
                        </div>
                    </a>
                    <a class="nav-link" href="{% url 'List_Employee' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="far fa-user"></span>
                            </span>
                            <span class="nav-link-text ps-1">Empleados</span>
                        </div>
                    </a>
                {% endif %}
            {% endfor %}
        {% endif %}
        <a class="nav-link dropdown-indicator" href="#report_invoice" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="report_invoice">
            <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="far fa-file-alt"></span></span><span class="nav-link-text ps-1">Reportes</span>
            </div>
        </a>
        <ul class="nav collapse false" id="report_invoice">
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura POS</span></div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura Electrónica</span></div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Crédito</span></div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Debito</span></div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Documento Soporte </span></div>
              </a>
            </li>                            
        </ul>

        <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
            <div class="col-auto navbar-vertical-label">Social</div>
            <div class="col ps-0">
              <hr class="mb-0 navbar-vertical-divider" />
            </div>
        </div>
        <a class="nav-link" href="javascript:void(0);" >
            <div class="d-flex align-items-center">
                <span class="nav-link-icon">
                    <span class="fas fa-envelope-open"></span>
                </span>
                <span class="nav-link-text ps-1">Inbox</span>
            </div>
        </a>
        {% if 1 == 5 %}
            <a class="nav-link" href="javascript:void(0);" >
                <div class="d-flex align-items-center">
                    <span class="nav-link-icon">
                        <span class="fab fa-reddit-alien"></span>
                    </span>
                    <span class="nav-link-text ps-1">Chat</span>
                </div>
            </a>
        {% endif %}
    </li>
    {% if request.session.permission %}
        {% for i in request.session.permission %}
            {% if i == "Todos" %}
                <li class="nav-item">
                    <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
                        <div class="col-auto navbar-vertical-label">Configuraciones</div>
                        <div class="col ps-0">
                          <hr class="mb-0 navbar-vertical-divider" />
                        </div>
                    </div>
                    <a class="nav-link" href="{% url 'Settings' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-cog"></span>
                            </span>
                            <span class="nav-link-text ps-1">Empresa</span>
                        </div>
                    </a>
                </li>
            {% endif %}
        {% endfor %}
    {% endif %}
    <!-- <li class="nav-item">
        <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
            <div class="col-auto navbar-vertical-label">Social</div>
            <div class="col ps-0">
              <hr class="mb-0 navbar-vertical-divider" />
            </div>
        </div>
        <a class="nav-link dropdown-indicator" href="#social" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="social">
            <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-share-alt"></span></span><span class="nav-link-text ps-1">Email</span>
            </div>
          </a>
          <ul class="nav collapse false" id="social">
            <li class="nav-item"><a class="nav-link" href="{% url 'Index' %}" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Inicio</span>
                </div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Chat</span>
                </div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Seguidores</span>
                </div>
              </a>
            </li>
          </ul>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="" >
            <div class="d-flex align-items-center">
                <span class="nav-link-icon">
                    <span class="fas fa-shopping-cart"></span>
                </span>
                <span class="nav-link-text ps-1">Marketplace</span>
            </div>
          </a>
    </li> -->
    
    <!-- <li class="nav-item">
       
      <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
        <div class="col-auto navbar-vertical-label">Aplicaciones
        </div>
        <div class="col ps-0">
          <hr class="mb-0 navbar-vertical-divider" />
        </div>
      </div>
      <a class="nav-link dropdown-indicator" href="#events" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="events">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-calendar-day"></span></span><span class="nav-link-text ps-1">Events</span>
        </div>
      </a>
      <ul class="nav collapse false" id="events">
            <li class="nav-item"><a class="nav-link" href="app/events/create-an-event.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Create an event</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="app/events/event-detail.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Event detail</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="app/events/event-list.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Event list</span>
                </div>
              </a>
               
            </li>
      </ul>
       
       
    </li> -->
    
    <!-- <li class="nav-item">
        <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
            <div class="col-auto navbar-vertical-label">Categorias</div>
            <div class="col ps-0">
              <hr class="mb-0 navbar-vertical-divider" />
            </div>
        </div>
        <a class="nav-link dropdown-indicator" href="#Categorias" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="social">
            <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-share-alt"></span></span><span class="nav-link-text ps-1">Social</span>
            </div>
          </a>
          <ul class="nav collapse false" id="Categorias">
            <li class="nav-item"><a class="nav-link" href="app/social/feed.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Chat</span>
                </div>
              </a>
            </li>
          </ul>
    </li> -->
    <!-- <li class="nav-item">
       
      <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
        <div class="col-auto navbar-vertical-label">Pages
        </div>
        <div class="col ps-0">
          <hr class="mb-0 navbar-vertical-divider" />
        </div>
      </div>
       <a class="nav-link" href="pages/starter.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-flag"></span></span><span class="nav-link-text ps-1">Starter</span>
        </div>
      </a>
       <a class="nav-link" href="pages/landing.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-globe"></span></span><span class="nav-link-text ps-1">Landing</span>
        </div>
      </a>
       <a class="nav-link dropdown-indicator" href="#authentication" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="authentication">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-lock"></span></span><span class="nav-link-text ps-1">Authentication</span>
        </div>
      </a>
      <ul class="nav collapse false" id="authentication">
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#simple" data-bs-toggle="collapse" aria-expanded="false" aria-controls="authentication">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Simple</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="simple">
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/login.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Login</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/logout.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Logout</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/register.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Register</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/forgot-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Forgot password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/confirm-mail.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Confirm mail</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/reset-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Reset password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/lock-screen.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Lock screen</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#card" data-bs-toggle="collapse" aria-expanded="false" aria-controls="authentication">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Card</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="card">
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/login.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Login</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/logout.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Logout</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/register.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Register</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/forgot-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Forgot password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/confirm-mail.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Confirm mail</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/reset-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Reset password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/lock-screen.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Lock screen</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#split" data-bs-toggle="collapse" aria-expanded="false" aria-controls="authentication">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Split</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="split">
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/login.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Login</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/logout.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Logout</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/register.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Register</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/forgot-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Forgot password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/confirm-mail.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Confirm mail</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/reset-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Reset password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/lock-screen.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Lock screen</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/authentication/wizard.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Wizard</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="#authentication-modal" data-bs-toggle="modal" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Modal</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#user" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="user">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-user"></span></span><span class="nav-link-text ps-1">User</span>
        </div>
      </a>
      <ul class="nav collapse false" id="user">
        <li class="nav-item"><a class="nav-link" href="pages/user/profile.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Profile</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/user/settings.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Settings</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#pricing" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="pricing">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-tags"></span></span><span class="nav-link-text ps-1">Pricing</span>
        </div>
      </a>
      <ul class="nav collapse false" id="pricing">
        <li class="nav-item"><a class="nav-link" href="pages/pricing/pricing-default.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pricing default</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/pricing/pricing-alt.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pricing alt</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#faq" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="faq">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-question-circle"></span></span><span class="nav-link-text ps-1">Faq</span>
        </div>
      </a>
      <ul class="nav collapse false" id="faq">
        <li class="nav-item"><a class="nav-link" href="pages/faq/faq-basic.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Faq basic</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/faq/faq-alt.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Faq alt</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/faq/faq-accordion.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Faq accordion</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#errors" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="errors">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-exclamation-triangle"></span></span><span class="nav-link-text ps-1">Errors</span>
        </div>
      </a>
      <ul class="nav collapse false" id="errors">
        <li class="nav-item"><a class="nav-link" href="pages/errors/404.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">404</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/errors/500.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">500</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#miscellaneous" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="miscellaneous">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-thumbtack"></span></span><span class="nav-link-text ps-1">Miscellaneous</span>
        </div>
      </a>
      <ul class="nav collapse false" id="miscellaneous">
        <li class="nav-item"><a class="nav-link" href="pages/miscellaneous/associations.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Associations</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/miscellaneous/invite-people.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Invite people</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/miscellaneous/privacy-policy.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Privacy policy</span>
            </div>
          </a>
           
        </li>
      </ul>
    </li> -->
    <!-- <li class="nav-item">
       
      <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
        <div class="col-auto navbar-vertical-label">Modules
        </div>
        <div class="col ps-0">
          <hr class="mb-0 navbar-vertical-divider" />
        </div>
      </div>
       <a class="nav-link dropdown-indicator" href="#forms" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="forms">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-file-alt"></span></span><span class="nav-link-text ps-1">Forms</span>
        </div>
      </a>
      <ul class="nav collapse false" id="forms">
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#basic" data-bs-toggle="collapse" aria-expanded="false" aria-controls="forms">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Basic</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="basic">
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/form-control.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Form control</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/input-group.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Input group</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/select.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Select</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/checks.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Checks</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/range.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Range</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/layout.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Layout</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#advance" data-bs-toggle="collapse" aria-expanded="false" aria-controls="forms">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Advance</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="advance">
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/advance-select.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Advance select</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/date-picker.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Date picker</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/editor.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Editor</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/emoji-button.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Emoji button</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/file-uploader.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">File uploader</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/rating.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Rating</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/forms/floating-labels.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Floating labels</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/forms/wizard.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Wizard</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/forms/validation.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Validation</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#tables" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="tables">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-table"></span></span><span class="nav-link-text ps-1">Tables</span>
        </div>
      </a>
      <ul class="nav collapse false" id="tables">
        <li class="nav-item"><a class="nav-link" href="modules/tables/basic-tables.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Basic tables</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/tables/advance-tables.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Advance tables</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/tables/bulk-select.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Bulk select</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#charts" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="charts">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-chart-line"></span></span><span class="nav-link-text ps-1">Charts</span>
        </div>
      </a>
      <ul class="nav collapse false" id="charts">
        <li class="nav-item"><a class="nav-link" href="modules/charts/chartjs.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Chartjs</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#eCharts" data-bs-toggle="collapse" aria-expanded="false" aria-controls="charts">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">ECharts</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="eCharts">
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/line-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Line charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/bar-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Bar charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/candlestick-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Candlestick charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/geo-map.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Geo map</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/scatter-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Scatter charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/pie-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pie charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/radar-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Radar charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/heatmap-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Heatmap charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/how-to-use.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">How to use</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#icons" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="icons">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-shapes"></span></span><span class="nav-link-text ps-1">Icons</span>
        </div>
      </a>
      <ul class="nav collapse false" id="icons">
        <li class="nav-item"><a class="nav-link" href="modules/icons/font-awesome.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Font awesome</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/icons/bootstrap-icons.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Bootstrap icons</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/icons/feather.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Feather</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/icons/material-icons.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Material icons</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#maps" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="maps">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-map"></span></span><span class="nav-link-text ps-1">Maps</span>
        </div>
      </a>
      <ul class="nav collapse false" id="maps">
        <li class="nav-item"><a class="nav-link" href="modules/maps/google-map.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Google map</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/maps/leaflet-map.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Leaflet map</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#components" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-puzzle-piece"></span></span><span class="nav-link-text ps-1">Components</span>
        </div>
      </a>
      <ul class="nav collapse false" id="components">
        <li class="nav-item"><a class="nav-link" href="modules/components/accordion.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Accordion</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/alerts.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Alerts</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/anchor.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Anchor</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/animated-icons.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Animated icons</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/background.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Background</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/badges.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Badges</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/breadcrumbs.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Breadcrumbs</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/buttons.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Buttons</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/calendar.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Calendar</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/cards.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Cards</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#carousel" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Carousel</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="carousel">
            <li class="nav-item"><a class="nav-link" href="modules/components/carousel/bootstrap.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Bootstrap</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/carousel/swiper.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Swiper</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/collapse.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Collapse</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/cookie-notice.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Cookie notice</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/countup.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Countup</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/draggable.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Draggable</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/dropdowns.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Dropdowns</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/list-group.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">List group</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/modals.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Modals</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#navs-_and_-Tabs" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Navs &amp; Tabs</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="navs-_and_-Tabs">
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/navs.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Navs</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/navbar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Navbar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/vertical-navbar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Vertical navbar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/top-navbar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Top navbar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/combo-navbar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Combo navbar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/tabs.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Tabs</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/offcanvas.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Offcanvas</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#pictures" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pictures</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="pictures">
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/avatar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Avatar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/images.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Images</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/figures.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Figures</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/hoverbox.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Hoverbox</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/lightbox.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Lightbox</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/progress-bar.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Progress bar</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/placeholder.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Placeholder</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/pagination.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pagination</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/popovers.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Popovers</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/scrollspy.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Scrollspy</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/search.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Search</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/spinners.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Spinners</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/toasts.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Toasts</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/tooltips.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Tooltips</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/treeview.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Treeview</span><span class="badge rounded-pill ms-2 badge-soft-success">New</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/typed-text.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Typed text</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#videos" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Videos</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="videos">
            <li class="nav-item"><a class="nav-link" href="modules/components/videos/embed.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Embed</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/videos/plyr.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Plyr</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#utilities" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="utilities">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-fire"></span></span><span class="nav-link-text ps-1">Utilities</span>
        </div>
      </a>
      <ul class="nav collapse false" id="utilities">
        <li class="nav-item"><a class="nav-link" href="modules/utilities/borders.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Borders</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/clearfix.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Clearfix</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/colors.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Colors</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/colored-links.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Colored links</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/display.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Display</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/flex.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Flex</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/float.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Float</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/grid.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Grid</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/overlayscrollbars.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Overlayscrollbars</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/position.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Position</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/spacing.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Spacing</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/sizing.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Sizing</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/stretched-link.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Stretched link</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/text-truncation.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Text truncation</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/typography.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Typography</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/vertical-align.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Vertical align</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/visibility.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Visibility</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link" href="widgets.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-poll"></span></span><span class="nav-link-text ps-1">Widgets</span>
        </div>
      </a>
       <a class="nav-link dropdown-indicator" href="#multi-level" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="multi-level">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-layer-group"></span></span><span class="nav-link-text ps-1">Multi level</span>
        </div>
      </a>
      <ul class="nav collapse false" id="multi-level">
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#level-two" data-bs-toggle="collapse" aria-expanded="false" aria-controls="multi-level">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Level two</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="level-two">
            <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 1</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 2</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#level-three" data-bs-toggle="collapse" aria-expanded="false" aria-controls="multi-level">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Level three</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="level-three">
            <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 3</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link dropdown-indicator" href="#item-4" data-bs-toggle="collapse" aria-expanded="false" aria-controls="level-three">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 4</span>
                </div>
              </a>
               
              <ul class="nav collapse false" id="item-4">
                <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                    <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 5</span>
                    </div>
                  </a>
                   
                </li>
                <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                    <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 6</span>
                    </div>
                  </a>
                   
                </li>
              </ul>
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#level-four" data-bs-toggle="collapse" aria-expanded="false" aria-controls="multi-level">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Level four</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="level-four">
            <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 6</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link dropdown-indicator" href="#item-7" data-bs-toggle="collapse" aria-expanded="false" aria-controls="level-four">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 7</span>
                </div>
              </a>
               
              <ul class="nav collapse false" id="item-7">
                <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                    <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 8</span>
                    </div>
                  </a>
                   
                </li>
                <li class="nav-item"><a class="nav-link dropdown-indicator" href="#item-9" data-bs-toggle="collapse" aria-expanded="false" aria-controls="item-7">
                    <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 9</span>
                    </div>
                  </a>
                   
                  <ul class="nav collapse false" id="item-9">
                    <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                        <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 10</span>
                        </div>
                      </a>
                       
                    </li>
                    <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                        <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 11</span>
                        </div>
                      </a>
                       
                    </li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </li>
    <li class="nav-item">
       
      <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
        <div class="col-auto navbar-vertical-label">Documentation
        </div>
        <div class="col ps-0">
          <hr class="mb-0 navbar-vertical-divider" />
        </div>
      </div>
       <a class="nav-link" href="documentation/getting-started.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-rocket"></span></span><span class="nav-link-text ps-1">Getting started</span>
        </div>
      </a>
       <a class="nav-link dropdown-indicator" href="#customization" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="customization">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-wrench"></span></span><span class="nav-link-text ps-1">Customization</span>
        </div>
      </a>
      <ul class="nav collapse false" id="customization">
        <li class="nav-item"><a class="nav-link" href="documentation/customization/configuration.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Configuration</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="documentation/customization/styling.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Styling</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="documentation/customization/dark-mode.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Dark mode</span><span class="badge rounded-pill ms-2 badge-soft-success">New</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="documentation/customization/plugin.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Plugin</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link" href="documentation/gulp.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fab fa-gulp"></span></span><span class="nav-link-text ps-1">Gulp</span>
        </div>
      </a>
       <a class="nav-link" href="documentation/design-file.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-palette"></span></span><span class="nav-link-text ps-1">Design file</span>
        </div>
      </a>
       <a class="nav-link" href="changelog.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-code-branch"></span></span><span class="nav-link-text ps-1">Changelog</span>
        </div>
      </a>
    </li> -->
  </ul>
  
</div>
</div>
"""


HTML_EMAIL = """
    <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width,initial-scale=1">
            <meta name="x-apple-disable-message-reformatting">
            <title></title>
            <!--[if mso]>
            <noscript>
                <xml>
                    <o:OfficeDocumentSettings>
                        <o:PixelsPerInch>96</o:PixelsPerInch>
                    </o:OfficeDocumentSettings>
                </xml>
            </noscript>
            <![endif]-->
            <style>
                table, td, div, h1, p {font-family: Arial, sans-serif;}

                .boton-personalizado-5 {
                    margin:0 0 25px 0;
                    font-size:16px;
                    line-height:24px;
                    font-family:Arial,sans-serif;
                    text-decoration:none;
                    font-weight: 600;
                    font-size: 20px;
                    color:#ffffff;
                    padding-top:15px;
                    padding-bottom:15px;
                    padding-left:40px;
                    padding-right:40px;
                    background-color:#f2595e;
                    border-color: #F69DA1;
                    border-width: 3px;
                    border-style: solid;
                }

                .boton-personalizado-6 {
                    margin:0 0 25px 0;
                    font-size:16px;
                    line-height:24px;
                    font-family:Arial,sans-serif;
                    text-decoration:none;
                    font-weight: 600;
                    font-size: 20px;
                    color:#ffffff;
                    padding-top:15px;
                    padding-bottom:15px;
                    padding-left:40px;
                    padding-right:40px;
                    background-color:#f2595e;
                    border-color: #F69DA1;
                    border-width: 3px;
                    border-style: solid;
                }


            </style>
        </head>
        <body style="margin:0;padding:0;">
            <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
                <tr>
                    <td align="center" style="padding:0;">
                        <table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                            <tr>
                                <td align="center" style="padding:40px 0 30px 0;background:#70bbd9;">
                                    <img src="$(logo)" alt="" width="300" style="height:auto;display:block;" />
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding:40px 0 30px 0;background:#70bbd9;">
                                    <img src="letras.png" alt="" width="300" style="height:auto;display:block;">
                                </td>
                            </tr>
                            <tr>
                                <td style="padding:36px 30px 42px 30px;">
                                    <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                        <tr>
                                            <td style="padding:0 0 36px 0;color:#153643;">
                                                <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">
                                                    Hola $(client_name)!. Por medio de la presente, le mandamos los documentos correspondientes a la $(type_document) N° $(invoice_number). Por favor antes de seleccionar alguna de las opciones siguientes, verificar los documentos que se le han adjuntado.
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding:0;">
                                                <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                                    <tr>
                                                        <td style="width:260px;padding:0;vertical-align:top;color:#153643;">
                                                            <a style="text-decoration:none; color:white;" class="boton-personalizado-5" href="http://theriosoft.com:8080/customerlogin/$(nit_company)/$(nit_customer)">ACEPTAR</a>
                                                        </td>
                                                        <td style="width:20px;padding:0;font-size:0;line-height:0;">&nbsp;</td>
                                                        <td style="width:260px;padding:0;vertical-align:top;color:#153643;">
                                                            <a style="text-decoration:none; color:white;" class="boton-personalizado-6" href="https://theriosoft.com/Rechazo/$(invoice_number)/$(pk_company)">RECHAZO</a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding:30px;background:#ee4c50;">
                                    <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;font-size:9px;font-family:Arial,sans-serif;">
                                        <tr>
                                            <td style="padding:0;width:50%;" align="left">
                                                <p style="margin:0;font-size:14px;line-height:16px;font-family:Arial,sans-serif;color:#ffffff;">
                                                    &reg; 2023<br/><a href="https://theriosoft.com" style="color:#ffffff;text-decoration:underline;">Theriosoft s.a.s</a>
                                                </p>
                                            </td>
                                            <td style="padding:0;width:50%;" align="right">
                                                <table role="presentation" style="border-collapse:collapse;border:0;border-spacing:0;">
                                                    <tr>
                                                        <td style="padding:0 0 0 10px;width:38px;">
                                                            <a href="https://www.facebook.com/theriosoft.med/" style="color:#ffffff;"><img src="https://assets.codepen.io/210284/fb_1.png" alt="Facebook" width="38" style="height:auto;display:block;border:0;" />
                                                            </a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
    </html>
"""
=======
from getpass import getuser
USER_WINDOWS = getuser()

URL_SERVER = "http://26.246.95.16:9090"
#URL_SERVER = "http://127.0.0.1:9797"
#URL_SERVER = "https://apievansoft.pythonanywhere.com"

URL_APPLICATION = "http://26.246.95.16:80"
#URL_APPLICATION = "http://127.0.0.1:8000"
# URL_APPLICATION = "http://26.246.95.16:80"
#URL_APPLICATION = "https://facturaevansoft.pythonanywhere.com"


# URL_FILES_SERVER = f"C:/Users/{USER_WINDOWS}/Documents/Project/invoice/static/company/"
URL_FILES_SERVER = f"C:/Users/Public/Videos/Nueva carpeta (2)/evangeli/static/company/"
# URL_FILES_SERVER = "/home/facturaevansoft/invoice_new_evansoft/static/company/"

# URL_FILES_TEMPLATE = f"C:/Users/{USER_WINDOWS}/Documents/Project/invoice/template"
URL_FILES_TEMPLATE = f"C:/Users/Public/Videos/Nueva carpeta (2)/evangeli/template"
# URL_FILES_TEMPLATE = "/home/facturaevansoft/invoice_new_evansoft/template"


#URL_UNIVERSAL
#**************************************************************************************************************************************************************************************************************

URL_IN_USE = URL_SERVER
URL_FILES = URL_FILES_SERVER
URL_FILES_TEMPLATE = URL_FILES_TEMPLATE

#**************************************************************************************************************************************************************************************************************


#AUTHENTICATION 

LOGIN = f"{URL_IN_USE}/user/Login/"
LOGOUT = f"{URL_IN_USE}/user/LogOut/"

#SUPPLIER

LIST_SUPPLIER = f"{URL_IN_USE}/inventory/List_Supplier/"
CREATE_SUPPLIER = f"{URL_IN_USE}/inventory/Create_Supplier/"
DELETE_SUPPLIER = f"{URL_IN_USE}/inventory/Delete_Supplier/"
GET_SUPPLIER = f"{URL_IN_USE}/inventory/Get_Supplier/"
UPDATE_SUPPLIER = f"{URL_IN_USE}/inventory/Update_Supplier/"
GET_LIST_BEST_SELLING_PRODUCT = f"{URL_IN_USE}/inventory/Get_List_Best_Selling_Product/"
GET_ALL_LIST_BEST_SELLING_PRODUCT = f"{URL_IN_USE}/inventory/Get_All_List_Best_Selling_Product/"

#EMPLOYEE

CREATE_EMPLOYEE = f"{URL_IN_USE}/user/Create_Employee/"
GET_EMPLOYEE = f"{URL_IN_USE}/user/Get_Employee/"
DELETE_USER = f"{URL_IN_USE}/user/Delete_User/"
UPDATE_USER = f"{URL_IN_USE}/user/Update_User/"
GET_LIST_EMPLOYEE = f"{URL_IN_USE}/user/Get_List_Employee/"
QUERY_PERMISSIONS = f"{URL_IN_USE}/user/Query_Permissions/"
GET_LIST_EMAIL = f"{URL_IN_USE}/user/Get_List_Email/"

#INVENTORY

GET_LIST_PRODUCTS = f"{URL_IN_USE}/inventory/Get_List_Products/"
CREATE_PRODUCT = f"{URL_IN_USE}/inventory/Create_Product/"
DELETE_PRODUCT = f"{URL_IN_USE}/inventory/Delete_Product/"
GET_PRODUCT = f"{URL_IN_USE}/inventory/Get_Product/"
UPDATE_PRODUCT = f"{URL_IN_USE}/inventory/Update_Product/"
GET_LIST_PRODUCTS_SUPPLIER = f"{URL_IN_USE}/inventory/Get_List_Products_Supplier/"
PRODUCT_RESERVED_USER = f"{URL_IN_USE}/inventory/Product_Reserved_User/"
RETURN_PRODUCTS = f"{URL_IN_USE}/inventory/Return_Products/"
RETURN_PRODUCT_UNIQUE = f"{URL_IN_USE}/inventory/return_product_UNIQUE/"
VALIDATED_QUANTITY = f"{URL_IN_USE}/inventory/Validated_Quantity/"
LIST_BRANCH = f"{URL_IN_USE}/company/List_Branch/"
SAVE_TRANSFER = f"{URL_IN_USE}/transfers/Save_Transfer/"

CREATE_CATEGORY = f"{URL_IN_USE}/inventory/Create_Category/"
CREATE_SUBCATEGORY = f"{URL_IN_USE}/inventory/Create_Subcategory/"
GET_CATEGORY = f"{URL_IN_USE}/inventory/Get_Category/"
GET_SUBCATEGORY = f"{URL_IN_USE}/inventory/Get_SubCategory/"


#SHOPPING

VERIFIED_INVOICE = f"{URL_IN_USE}/shopping/Verified_Invoice/"
CREATE_SHOPPING = f"{URL_IN_USE}/shopping/Create_Shopping/"


#CUSTOMER

GET_LIST_CUSTOMER = f"{URL_IN_USE}/customer/Get_List_Customer/"
GET_CUSTOMER = f"{URL_IN_USE}/customer/Get_Customer/"
UPDATE_CUSTOMER = f"{URL_IN_USE}/customer/Update_Customer/"
CREATE_CUSTOMER = f"{URL_IN_USE}/customer/Create_Customer/"
DELETE_CLIENT = f"{URL_IN_USE}/customer/Delete_Client/"

#INVOICE

GET_LIST_INVOICE = f"{URL_IN_USE}/invoice/Get_List_Invoice/"
ANNULLED_INVOICE = f"{URL_IN_USE}/invoice/Annulled_Invoice/"
GET_INVOICE = f"{URL_IN_USE}/invoice/Get_Invoice/"
CREATE_INVOICE = f"{URL_IN_USE}/invoice/Create_Invoice/"
GET_SELLING_BY_INVOICE = f"{URL_IN_USE}/invoice/Get_Selling_By_Invoice/"
GET_SELLING_BY_DATE = f"{URL_IN_USE}/invoice/Get_Selling_By_Date/"
SEND_INVOICE_DIAN = f"{URL_IN_USE}/invoice/Send_Invoice_DIAN/"
ANNULLED_INVOICE_BY_PRODUCT = f"{URL_IN_USE}/invoice/Annulled_Invoice_By_Product/"
CREATE_PASS_INVOICE = f"{URL_IN_USE}/invoice/Create_Pass_Invoice/"

### THERIOSOFT
PDF_TO_BASE64 = "https://theriosoft.com/api/pdf_to_base64/"


#REPORT

REPORT_INVOICES = f"{URL_IN_USE}/report/Report_Invoices/"
REPORT_INVOICE_ANNULLED = f"{URL_IN_USE}/report/Report_Invoice_Annulled/"
CLOSE_THE_BOX_ALL = f"{URL_IN_USE}/report/Close_The_Box_All/"
HISTORY_INVENTORY = f"{URL_IN_USE}/report/History_Inventory/"


#SETTING

GET_TYPE_WORKER = f"{URL_IN_USE}/setting/Get_Type_Worker/"
GET_TYPE_CONTRACT = f"{URL_IN_USE}/setting/Get_Type_Contract/"
GET_TSUB_TYPE_WORKER = f"{URL_IN_USE}/setting/Get_TSub_Type_Worker/"
GET_PAYROLL_TYPE_DOCUMENT_IDENTIFICATION = f"{URL_IN_USE}/setting/Get_Payroll_Type_Document_Identification/"
GET_MUNICIPALITIES = f"{URL_IN_USE}/setting/Get_Municipalities/"
GET_PERMISSION = f"{URL_IN_USE}/setting/Get_Permission/"
GET_TYPE_DOCUMENT_I = f"{URL_IN_USE}/setting/Get_Type_Document_I/"
GET_TYPE_REGIMEN = f"{URL_IN_USE}/setting/Get_Type_Regimen/"
GET_ALL_UNIT_MEASURES = f"{URL_IN_USE}/setting/Get_All_Unit_Measures/"
GET_TYPE_ORGANIZATION = f"{URL_IN_USE}/setting/Get_Type_Organization/"
GET_RESOLUTION = f"{URL_IN_USE}/company/Get_Resolution/"
GET_BRANCH = f"{URL_IN_USE}/company/Get_Branch/"
GET_RESOLUTION_LIST = f"{URL_IN_USE}/company/Get_Resolution_List/"
UPDATE_RESOLUTION_DIAN = f"{URL_IN_USE}/company/Update_Resolution_DIAN/"
UPDATE_BRANCH = f"{URL_IN_USE}/company/Update_Branch/"
UPDATE_LOGO = f"{URL_IN_USE}/company/Update_Logo/"


#EMAIL

GET_LIST_EMAILS = f"{URL_IN_USE}/emails/Get_List_Emails/"
GET_LIST_EMAIL_SENDER = f"{URL_IN_USE}/emails/Get_List_Email_Sender/"
CREATE_EMAIL = f"{URL_IN_USE}/emails/Create_Email/"
GET_EMAIL = f"{URL_IN_USE}/emails/Get_Email/"
MARK_AS_READ = f"{URL_IN_USE}/emails/Mark_As_Read/"


#PAYROLL

GET_ALL_PAYROLL_EMPLOYEE = f"{URL_IN_USE}/payroll/Get_All_Payroll_Employee/"
BASIC_PAYROLL = f"{URL_IN_USE}/payroll/Basic_Payroll/"
DELETE_PAYROLL = f"{URL_IN_USE}/payroll/Delete_Payroll/"

#WALLET
GET_PASS_INVOICE = f"{URL_IN_USE}/wallet/Get_Pass_Invoice/"
GET_ALL_HISTORY_PASS_INVOICE = f"{URL_IN_USE}/wallet/Get_All_History_Pass_Invoice/"
GET_ALL_HISTORY_PASS_CUSTOMER = f"{URL_IN_USE}/wallet/Get_All_History_Pass_Customer/"



HTML_MENU = """
<div class="collapse navbar-collapse menu_mio" id="navbarVerticalCollapse">
<div class="navbar-vertical-content scrollbar">
  <ul class="navbar-nav flex-column mb-3" id="navbarVerticalNav">
    <li class="nav-item">
         
        {% if request.session.permission %}
            {% for i in request.session.permission %}
                {% if i == "Facturacion"  or i == "Todos" %}
                    <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
                        <div class="col-auto navbar-vertical-label">Operaciones</div>
                        <div class="col ps-0">
                          <hr class="mb-0 navbar-vertical-divider" />
                        </div>
                    </div>
                    <a class="nav-link dropdown-indicator" href="#events" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="events">
                        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="far fa-file-alt"></span></span><span class="nav-link-text ps-1">Crear Documentos</span>
                        </div>
                    </a>
                    <ul class="nav collapse false" id="events">
                        <li class="nav-item"><a class="nav-link" href="{% url 'Create_Invoice' %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura</span>
                            </div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Documento Soporte </span>
                            </div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Crédito</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Debito</span></div>
                          </a>
                        </li>
                    </ul>
                    <a class="nav-link dropdown-indicator" href="#document" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="document">
                        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="far fa-file-alt"></span></span><span class="nav-link-text ps-1">Documentos Generados</span>
                        </div>
                    </a>
                    <ul class="nav collapse false" id="document">
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 1 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura POS</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 2 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura Electrónica</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 3 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Crédito</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 4 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Debito</span></div>
                          </a>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Get_List_Invoice' 5 %}" aria-expanded="false">
                            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Documento Soporte </span></div>
                          </a>
                        </li>                            
                    </ul>
                {% endif %}
            {% endfor %}
        {% endif %}
    </li>
    <li class="nav-item">
        
        <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
            <div class="col-auto navbar-vertical-label">Administración</div>
            <div class="col ps-0">
              <hr class="mb-0 navbar-vertical-divider" />
            </div>
        </div>
        {% if request.session.permission %}
            {% for i in request.session.permission %}
                {% if i != "Contador" %}
                    <a class="nav-link" href="{% url 'Get_List_Customer' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-users"></span>
                            </span>
                            <span class="nav-link-text ps-1">Clientes</span>
                        </div>
                    </a>
                {% endif %}
            {% endfor %}
        {% endif %}
        {% if request.session.permission %}
            {% for i in request.session.permission %}
                {% if i == "Administrativo" or i == "Todos" or i == 'Creador' %}
                    <a class="nav-link" href="{% url 'Register_Purchase' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-shopping-cart"></span>
                            </span>
                            <span class="nav-link-text ps-1">Compras</span>
                        </div>
                    </a>
                    <a class="nav-link" href="{% url 'List_Supplier' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-users"></span>
                            </span>
                            <span class="nav-link-text ps-1">Proveedores</span>
                        </div>
                    </a>
                    <a class="nav-link" href="{% url 'Get_List_Products' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-archive"></span>
                            </span>
                            <span class="nav-link-text ps-1">Inventario</span>
                        </div>
                    </a>
                    <a class="nav-link" href="{% url 'Transfer' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-archive"></span>
                            </span>
                            <span class="nav-link-text ps-1">Traslados</span>
                        </div>
                    </a>
                    <a class="nav-link" href="{% url 'List_Employee' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="far fa-user"></span>
                            </span>
                            <span class="nav-link-text ps-1">Empleados</span>
                        </div>
                    </a>
                {% endif %}
            {% endfor %}
        {% endif %}
        <a class="nav-link dropdown-indicator" href="#report_invoice" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="report_invoice">
            <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="far fa-file-alt"></span></span><span class="nav-link-text ps-1">Reportes</span>
            </div>
        </a>
        <ul class="nav collapse false" id="report_invoice">
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura POS</span></div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Factura Electrónica</span></div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Crédito</span></div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Nota Debito</span></div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="javascript:void(0);" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Documento Soporte </span></div>
              </a>
            </li>                            
        </ul>

        <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
            <div class="col-auto navbar-vertical-label">Social</div>
            <div class="col ps-0">
              <hr class="mb-0 navbar-vertical-divider" />
            </div>
        </div>
        <a class="nav-link" href="javascript:void(0);" >
            <div class="d-flex align-items-center">
                <span class="nav-link-icon">
                    <span class="fas fa-envelope-open"></span>
                </span>
                <span class="nav-link-text ps-1">Inbox</span>
            </div>
        </a>
        {% if 1 == 5 %}
            <a class="nav-link" href="javascript:void(0);" >
                <div class="d-flex align-items-center">
                    <span class="nav-link-icon">
                        <span class="fab fa-reddit-alien"></span>
                    </span>
                    <span class="nav-link-text ps-1">Chat</span>
                </div>
            </a>
        {% endif %}
    </li>
    {% if request.session.permission %}
        {% for i in request.session.permission %}
            {% if i == "Todos" %}
                <li class="nav-item">
                    <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
                        <div class="col-auto navbar-vertical-label">Configuraciones</div>
                        <div class="col ps-0">
                          <hr class="mb-0 navbar-vertical-divider" />
                        </div>
                    </div>
                    <a class="nav-link" href="{% url 'Settings' %}" >
                        <div class="d-flex align-items-center">
                            <span class="nav-link-icon">
                                <span class="fas fa-cog"></span>
                            </span>
                            <span class="nav-link-text ps-1">Empresa</span>
                        </div>
                    </a>
                </li>
            {% endif %}
        {% endfor %}
    {% endif %}
    <!-- <li class="nav-item">
        <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
            <div class="col-auto navbar-vertical-label">Social</div>
            <div class="col ps-0">
              <hr class="mb-0 navbar-vertical-divider" />
            </div>
        </div>
        <a class="nav-link dropdown-indicator" href="#social" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="social">
            <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-share-alt"></span></span><span class="nav-link-text ps-1">Email</span>
            </div>
          </a>
          <ul class="nav collapse false" id="social">
            <li class="nav-item"><a class="nav-link" href="{% url 'Index' %}" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Inicio</span>
                </div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Chat</span>
                </div>
              </a>
            </li>
            <li class="nav-item"><a class="nav-link" href="" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Seguidores</span>
                </div>
              </a>
            </li>
          </ul>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="" >
            <div class="d-flex align-items-center">
                <span class="nav-link-icon">
                    <span class="fas fa-shopping-cart"></span>
                </span>
                <span class="nav-link-text ps-1">Marketplace</span>
            </div>
          </a>
    </li> -->
    
    <!-- <li class="nav-item">
       
      <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
        <div class="col-auto navbar-vertical-label">Aplicaciones
        </div>
        <div class="col ps-0">
          <hr class="mb-0 navbar-vertical-divider" />
        </div>
      </div>
      <a class="nav-link dropdown-indicator" href="#events" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="events">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-calendar-day"></span></span><span class="nav-link-text ps-1">Events</span>
        </div>
      </a>
      <ul class="nav collapse false" id="events">
            <li class="nav-item"><a class="nav-link" href="app/events/create-an-event.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Create an event</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="app/events/event-detail.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Event detail</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="app/events/event-list.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Event list</span>
                </div>
              </a>
               
            </li>
      </ul>
       
       
    </li> -->
    
    <!-- <li class="nav-item">
        <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
            <div class="col-auto navbar-vertical-label">Categorias</div>
            <div class="col ps-0">
              <hr class="mb-0 navbar-vertical-divider" />
            </div>
        </div>
        <a class="nav-link dropdown-indicator" href="#Categorias" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="social">
            <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-share-alt"></span></span><span class="nav-link-text ps-1">Social</span>
            </div>
          </a>
          <ul class="nav collapse false" id="Categorias">
            <li class="nav-item"><a class="nav-link" href="app/social/feed.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Chat</span>
                </div>
              </a>
            </li>
          </ul>
    </li> -->
    <!-- <li class="nav-item">
       
      <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
        <div class="col-auto navbar-vertical-label">Pages
        </div>
        <div class="col ps-0">
          <hr class="mb-0 navbar-vertical-divider" />
        </div>
      </div>
       <a class="nav-link" href="pages/starter.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-flag"></span></span><span class="nav-link-text ps-1">Starter</span>
        </div>
      </a>
       <a class="nav-link" href="pages/landing.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-globe"></span></span><span class="nav-link-text ps-1">Landing</span>
        </div>
      </a>
       <a class="nav-link dropdown-indicator" href="#authentication" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="authentication">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-lock"></span></span><span class="nav-link-text ps-1">Authentication</span>
        </div>
      </a>
      <ul class="nav collapse false" id="authentication">
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#simple" data-bs-toggle="collapse" aria-expanded="false" aria-controls="authentication">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Simple</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="simple">
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/login.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Login</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/logout.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Logout</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/register.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Register</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/forgot-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Forgot password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/confirm-mail.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Confirm mail</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/reset-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Reset password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/simple/lock-screen.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Lock screen</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#card" data-bs-toggle="collapse" aria-expanded="false" aria-controls="authentication">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Card</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="card">
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/login.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Login</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/logout.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Logout</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/register.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Register</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/forgot-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Forgot password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/confirm-mail.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Confirm mail</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/reset-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Reset password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/card/lock-screen.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Lock screen</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#split" data-bs-toggle="collapse" aria-expanded="false" aria-controls="authentication">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Split</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="split">
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/login.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Login</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/logout.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Logout</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/register.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Register</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/forgot-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Forgot password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/confirm-mail.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Confirm mail</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/reset-password.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Reset password</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="pages/authentication/split/lock-screen.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Lock screen</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/authentication/wizard.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Wizard</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="#authentication-modal" data-bs-toggle="modal" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Modal</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#user" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="user">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-user"></span></span><span class="nav-link-text ps-1">User</span>
        </div>
      </a>
      <ul class="nav collapse false" id="user">
        <li class="nav-item"><a class="nav-link" href="pages/user/profile.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Profile</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/user/settings.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Settings</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#pricing" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="pricing">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-tags"></span></span><span class="nav-link-text ps-1">Pricing</span>
        </div>
      </a>
      <ul class="nav collapse false" id="pricing">
        <li class="nav-item"><a class="nav-link" href="pages/pricing/pricing-default.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pricing default</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/pricing/pricing-alt.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pricing alt</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#faq" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="faq">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-question-circle"></span></span><span class="nav-link-text ps-1">Faq</span>
        </div>
      </a>
      <ul class="nav collapse false" id="faq">
        <li class="nav-item"><a class="nav-link" href="pages/faq/faq-basic.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Faq basic</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/faq/faq-alt.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Faq alt</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/faq/faq-accordion.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Faq accordion</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#errors" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="errors">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-exclamation-triangle"></span></span><span class="nav-link-text ps-1">Errors</span>
        </div>
      </a>
      <ul class="nav collapse false" id="errors">
        <li class="nav-item"><a class="nav-link" href="pages/errors/404.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">404</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/errors/500.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">500</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#miscellaneous" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="miscellaneous">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-thumbtack"></span></span><span class="nav-link-text ps-1">Miscellaneous</span>
        </div>
      </a>
      <ul class="nav collapse false" id="miscellaneous">
        <li class="nav-item"><a class="nav-link" href="pages/miscellaneous/associations.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Associations</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/miscellaneous/invite-people.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Invite people</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="pages/miscellaneous/privacy-policy.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Privacy policy</span>
            </div>
          </a>
           
        </li>
      </ul>
    </li> -->
    <!-- <li class="nav-item">
       
      <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
        <div class="col-auto navbar-vertical-label">Modules
        </div>
        <div class="col ps-0">
          <hr class="mb-0 navbar-vertical-divider" />
        </div>
      </div>
       <a class="nav-link dropdown-indicator" href="#forms" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="forms">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-file-alt"></span></span><span class="nav-link-text ps-1">Forms</span>
        </div>
      </a>
      <ul class="nav collapse false" id="forms">
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#basic" data-bs-toggle="collapse" aria-expanded="false" aria-controls="forms">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Basic</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="basic">
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/form-control.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Form control</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/input-group.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Input group</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/select.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Select</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/checks.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Checks</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/range.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Range</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/basic/layout.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Layout</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#advance" data-bs-toggle="collapse" aria-expanded="false" aria-controls="forms">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Advance</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="advance">
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/advance-select.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Advance select</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/date-picker.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Date picker</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/editor.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Editor</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/emoji-button.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Emoji button</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/file-uploader.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">File uploader</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/forms/advance/rating.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Rating</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/forms/floating-labels.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Floating labels</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/forms/wizard.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Wizard</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/forms/validation.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Validation</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#tables" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="tables">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-table"></span></span><span class="nav-link-text ps-1">Tables</span>
        </div>
      </a>
      <ul class="nav collapse false" id="tables">
        <li class="nav-item"><a class="nav-link" href="modules/tables/basic-tables.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Basic tables</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/tables/advance-tables.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Advance tables</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/tables/bulk-select.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Bulk select</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#charts" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="charts">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-chart-line"></span></span><span class="nav-link-text ps-1">Charts</span>
        </div>
      </a>
      <ul class="nav collapse false" id="charts">
        <li class="nav-item"><a class="nav-link" href="modules/charts/chartjs.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Chartjs</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#eCharts" data-bs-toggle="collapse" aria-expanded="false" aria-controls="charts">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">ECharts</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="eCharts">
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/line-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Line charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/bar-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Bar charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/candlestick-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Candlestick charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/geo-map.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Geo map</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/scatter-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Scatter charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/pie-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pie charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/radar-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Radar charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/heatmap-charts.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Heatmap charts</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/charts/echarts/how-to-use.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">How to use</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#icons" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="icons">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-shapes"></span></span><span class="nav-link-text ps-1">Icons</span>
        </div>
      </a>
      <ul class="nav collapse false" id="icons">
        <li class="nav-item"><a class="nav-link" href="modules/icons/font-awesome.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Font awesome</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/icons/bootstrap-icons.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Bootstrap icons</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/icons/feather.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Feather</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/icons/material-icons.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Material icons</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#maps" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="maps">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-map"></span></span><span class="nav-link-text ps-1">Maps</span>
        </div>
      </a>
      <ul class="nav collapse false" id="maps">
        <li class="nav-item"><a class="nav-link" href="modules/maps/google-map.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Google map</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/maps/leaflet-map.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Leaflet map</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#components" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-puzzle-piece"></span></span><span class="nav-link-text ps-1">Components</span>
        </div>
      </a>
      <ul class="nav collapse false" id="components">
        <li class="nav-item"><a class="nav-link" href="modules/components/accordion.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Accordion</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/alerts.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Alerts</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/anchor.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Anchor</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/animated-icons.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Animated icons</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/background.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Background</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/badges.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Badges</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/breadcrumbs.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Breadcrumbs</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/buttons.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Buttons</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/calendar.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Calendar</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/cards.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Cards</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#carousel" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Carousel</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="carousel">
            <li class="nav-item"><a class="nav-link" href="modules/components/carousel/bootstrap.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Bootstrap</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/carousel/swiper.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Swiper</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/collapse.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Collapse</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/cookie-notice.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Cookie notice</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/countup.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Countup</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/draggable.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Draggable</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/dropdowns.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Dropdowns</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/list-group.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">List group</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/modals.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Modals</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#navs-_and_-Tabs" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Navs &amp; Tabs</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="navs-_and_-Tabs">
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/navs.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Navs</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/navbar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Navbar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/vertical-navbar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Vertical navbar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/top-navbar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Top navbar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/combo-navbar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Combo navbar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/navs-and-tabs/tabs.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Tabs</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/offcanvas.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Offcanvas</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#pictures" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pictures</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="pictures">
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/avatar.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Avatar</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/images.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Images</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/figures.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Figures</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/hoverbox.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Hoverbox</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/pictures/lightbox.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Lightbox</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/progress-bar.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Progress bar</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/placeholder.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Placeholder</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/pagination.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Pagination</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/popovers.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Popovers</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/scrollspy.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Scrollspy</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/search.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Search</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/spinners.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Spinners</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/toasts.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Toasts</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/tooltips.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Tooltips</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/treeview.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Treeview</span><span class="badge rounded-pill ms-2 badge-soft-success">New</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/components/typed-text.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Typed text</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#videos" data-bs-toggle="collapse" aria-expanded="false" aria-controls="components">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Videos</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="videos">
            <li class="nav-item"><a class="nav-link" href="modules/components/videos/embed.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Embed</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="modules/components/videos/plyr.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Plyr</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
      </ul>
       <a class="nav-link dropdown-indicator" href="#utilities" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="utilities">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-fire"></span></span><span class="nav-link-text ps-1">Utilities</span>
        </div>
      </a>
      <ul class="nav collapse false" id="utilities">
        <li class="nav-item"><a class="nav-link" href="modules/utilities/borders.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Borders</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/clearfix.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Clearfix</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/colors.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Colors</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/colored-links.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Colored links</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/display.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Display</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/flex.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Flex</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/float.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Float</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/grid.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Grid</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/overlayscrollbars.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Overlayscrollbars</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/position.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Position</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/spacing.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Spacing</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/sizing.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Sizing</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/stretched-link.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Stretched link</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/text-truncation.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Text truncation</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/typography.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Typography</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/vertical-align.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Vertical align</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="modules/utilities/visibility.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Visibility</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link" href="widgets.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-poll"></span></span><span class="nav-link-text ps-1">Widgets</span>
        </div>
      </a>
       <a class="nav-link dropdown-indicator" href="#multi-level" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="multi-level">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-layer-group"></span></span><span class="nav-link-text ps-1">Multi level</span>
        </div>
      </a>
      <ul class="nav collapse false" id="multi-level">
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#level-two" data-bs-toggle="collapse" aria-expanded="false" aria-controls="multi-level">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Level two</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="level-two">
            <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 1</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 2</span>
                </div>
              </a>
               
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#level-three" data-bs-toggle="collapse" aria-expanded="false" aria-controls="multi-level">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Level three</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="level-three">
            <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 3</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link dropdown-indicator" href="#item-4" data-bs-toggle="collapse" aria-expanded="false" aria-controls="level-three">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 4</span>
                </div>
              </a>
               
              <ul class="nav collapse false" id="item-4">
                <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                    <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 5</span>
                    </div>
                  </a>
                   
                </li>
                <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                    <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 6</span>
                    </div>
                  </a>
                   
                </li>
              </ul>
            </li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link dropdown-indicator" href="#level-four" data-bs-toggle="collapse" aria-expanded="false" aria-controls="multi-level">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Level four</span>
            </div>
          </a>
           
          <ul class="nav collapse false" id="level-four">
            <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 6</span>
                </div>
              </a>
               
            </li>
            <li class="nav-item"><a class="nav-link dropdown-indicator" href="#item-7" data-bs-toggle="collapse" aria-expanded="false" aria-controls="level-four">
                <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 7</span>
                </div>
              </a>
               
              <ul class="nav collapse false" id="item-7">
                <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                    <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 8</span>
                    </div>
                  </a>
                   
                </li>
                <li class="nav-item"><a class="nav-link dropdown-indicator" href="#item-9" data-bs-toggle="collapse" aria-expanded="false" aria-controls="item-7">
                    <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 9</span>
                    </div>
                  </a>
                   
                  <ul class="nav collapse false" id="item-9">
                    <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                        <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 10</span>
                        </div>
                      </a>
                       
                    </li>
                    <li class="nav-item"><a class="nav-link" href="#!.html" aria-expanded="false">
                        <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Item 11</span>
                        </div>
                      </a>
                       
                    </li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </li>
    <li class="nav-item">
       
      <div class="row navbar-vertical-label-wrapper mt-3 mb-2">
        <div class="col-auto navbar-vertical-label">Documentation
        </div>
        <div class="col ps-0">
          <hr class="mb-0 navbar-vertical-divider" />
        </div>
      </div>
       <a class="nav-link" href="documentation/getting-started.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-rocket"></span></span><span class="nav-link-text ps-1">Getting started</span>
        </div>
      </a>
       <a class="nav-link dropdown-indicator" href="#customization" role="button" data-bs-toggle="collapse" aria-expanded="false" aria-controls="customization">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-wrench"></span></span><span class="nav-link-text ps-1">Customization</span>
        </div>
      </a>
      <ul class="nav collapse false" id="customization">
        <li class="nav-item"><a class="nav-link" href="documentation/customization/configuration.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Configuration</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="documentation/customization/styling.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Styling</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="documentation/customization/dark-mode.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Dark mode</span><span class="badge rounded-pill ms-2 badge-soft-success">New</span>
            </div>
          </a>
           
        </li>
        <li class="nav-item"><a class="nav-link" href="documentation/customization/plugin.html" aria-expanded="false">
            <div class="d-flex align-items-center"><span class="nav-link-text ps-1">Plugin</span>
            </div>
          </a>
           
        </li>
      </ul>
       <a class="nav-link" href="documentation/gulp.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fab fa-gulp"></span></span><span class="nav-link-text ps-1">Gulp</span>
        </div>
      </a>
       <a class="nav-link" href="documentation/design-file.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-palette"></span></span><span class="nav-link-text ps-1">Design file</span>
        </div>
      </a>
       <a class="nav-link" href="changelog.html" role="button" aria-expanded="false">
        <div class="d-flex align-items-center"><span class="nav-link-icon"><span class="fas fa-code-branch"></span></span><span class="nav-link-text ps-1">Changelog</span>
        </div>
      </a>
    </li> -->
  </ul>
  
</div>
</div>
"""


HTML_EMAIL = """
    <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width,initial-scale=1">
            <meta name="x-apple-disable-message-reformatting">
            <title></title>
            <!--[if mso]>
            <noscript>
                <xml>
                    <o:OfficeDocumentSettings>
                        <o:PixelsPerInch>96</o:PixelsPerInch>
                    </o:OfficeDocumentSettings>
                </xml>
            </noscript>
            <![endif]-->
            <style>
                table, td, div, h1, p {font-family: Arial, sans-serif;}

                .boton-personalizado-5 {
                    margin:0 0 25px 0;
                    font-size:16px;
                    line-height:24px;
                    font-family:Arial,sans-serif;
                    text-decoration:none;
                    font-weight: 600;
                    font-size: 20px;
                    color:#ffffff;
                    padding-top:15px;
                    padding-bottom:15px;
                    padding-left:40px;
                    padding-right:40px;
                    background-color:#f2595e;
                    border-color: #F69DA1;
                    border-width: 3px;
                    border-style: solid;
                }

                .boton-personalizado-6 {
                    margin:0 0 25px 0;
                    font-size:16px;
                    line-height:24px;
                    font-family:Arial,sans-serif;
                    text-decoration:none;
                    font-weight: 600;
                    font-size: 20px;
                    color:#ffffff;
                    padding-top:15px;
                    padding-bottom:15px;
                    padding-left:40px;
                    padding-right:40px;
                    background-color:#f2595e;
                    border-color: #F69DA1;
                    border-width: 3px;
                    border-style: solid;
                }


            </style>
        </head>
        <body style="margin:0;padding:0;">
            <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
                <tr>
                    <td align="center" style="padding:0;">
                        <table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
                            <tr>
                                <td align="center" style="padding:40px 0 30px 0;background:#70bbd9;">
                                    <img src="$(logo)" alt="" width="300" style="height:auto;display:block;" />
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding:40px 0 30px 0;background:#70bbd9;">
                                    <img src="letras.png" alt="" width="300" style="height:auto;display:block;">
                                </td>
                            </tr>
                            <tr>
                                <td style="padding:36px 30px 42px 30px;">
                                    <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                        <tr>
                                            <td style="padding:0 0 36px 0;color:#153643;">
                                                <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">
                                                    Hola $(client_name)!. Por medio de la presente, le mandamos los documentos correspondientes a la $(type_document) N° $(invoice_number). Por favor antes de seleccionar alguna de las opciones siguientes, verificar los documentos que se le han adjuntado.
                                                </p>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="padding:0;">
                                                <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                                                    <tr>
                                                        <td style="width:260px;padding:0;vertical-align:top;color:#153643;">
                                                            <a style="text-decoration:none; color:white;" class="boton-personalizado-5" href="http://theriosoft.com:8080/customerlogin/$(nit_company)/$(nit_customer)">ACEPTAR</a>
                                                        </td>
                                                        <td style="width:20px;padding:0;font-size:0;line-height:0;">&nbsp;</td>
                                                        <td style="width:260px;padding:0;vertical-align:top;color:#153643;">
                                                            <a style="text-decoration:none; color:white;" class="boton-personalizado-6" href="https://theriosoft.com/Rechazo/$(invoice_number)/$(pk_company)">RECHAZO</a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td style="padding:30px;background:#ee4c50;">
                                    <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;font-size:9px;font-family:Arial,sans-serif;">
                                        <tr>
                                            <td style="padding:0;width:50%;" align="left">
                                                <p style="margin:0;font-size:14px;line-height:16px;font-family:Arial,sans-serif;color:#ffffff;">
                                                    &reg; 2023<br/><a href="https://theriosoft.com" style="color:#ffffff;text-decoration:underline;">Theriosoft s.a.s</a>
                                                </p>
                                            </td>
                                            <td style="padding:0;width:50%;" align="right">
                                                <table role="presentation" style="border-collapse:collapse;border:0;border-spacing:0;">
                                                    <tr>
                                                        <td style="padding:0 0 0 10px;width:38px;">
                                                            <a href="https://www.facebook.com/theriosoft.med/" style="color:#ffffff;"><img src="https://assets.codepen.io/210284/fb_1.png" alt="Facebook" width="38" style="height:auto;display:block;border:0;" />
                                                            </a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
    </html>
"""
>>>>>>> fcce1250637949c4253f5212ecfaac71d2f5683d
