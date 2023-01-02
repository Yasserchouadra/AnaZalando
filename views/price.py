from dash import dcc,html
import dash_bootstrap_components as dbc
from dash import Input, Output,  html,State
from maindash import app




from mycontrollers.preprocessing import get_df_products
from mycontrollers.preprocessing import select_products


from views.product import make_product_card

from mycontrollers.priceController import propose_best_products
from mycontrollers.priceController import select_moins_cher
from mycontrollers.priceController import select_moyens_products
from mycontrollers.priceController import select_plus_cher


df = get_df_products()
selected_df = select_products(df,"chemise","homme", "all")






def make_list_prods (df_products):
      list_cards = []
      for k, v in df_products.iterrows():
         list_cards.append( make_product_card(v["product"],v["description"],v["sexe"],v["mark"],v["picture"],str(v["finalprice"]),str(v["originprice"]),str(v["promo"])+ "%") )
      return list_cards

def price(choice):
      if choice == "best":
            df_products =  propose_best_products(selected_df)
      elif choice == "cheap":
            df_products =  select_moins_cher(selected_df)
      elif choice == "average":
            df_products =  select_moyens_products(selected_df)
      elif choice == "expensive":
            df_products =  select_plus_cher(selected_df)
      else :
            df_products =  propose_best_products(selected_df)

      return   html.Div(
                        [
                              html.H3("This the list of the products with "+choice + " price ! " ),
                              html.Br(),
                              html.Div( make_list_prods(df_products))
                        ]
                         )
    
