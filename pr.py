import streamlit as st
# Data handling dependencies


def main():
# Page config
  st.set_page_config(page_title='Currency Arbitrage App', page_icon='📈') 

  # Page title
  st.title('Currency Arbitrage App')

    #Inputs section
  with st.form('inputs'):

      st.header('Inputs')

      col1, col2 = st.columns(2)

      with col1:
          initial_gbp = st.number_input('Initial amount (GBP)', min_value=0.0, value=10.0, key='initial')
          kes_per_gbp = st.number_input('KES per 1 GBP(Lemonade Rates)', min_value=0.0, value=185.0, key='kes_gbp')

      with col2:  
          usdt_per_kes = st.number_input('USDT per 1 KES(Kenyan Sellers Rate)', min_value=0.0, value=140.99, key='usdt_kes')
          gbp_per_usdt = st.number_input('GBP per 1 USDT(revolut/monzo/wise rate)', min_value=0.0, value=0.782, key='gbp_usdt')

      submitted = st.form_submit_button('Submit')

  if submitted:

      # Calculations
      kes_amount = initial_gbp * kes_per_gbp  
      usdt_amount = kes_amount / usdt_per_kes
      final_gbp = usdt_amount * gbp_per_usdt  
      profit_loss = final_gbp - initial_gbp

      # Results section
      st.header('Results')
      st.markdown('---')

      col1, col2 = st.columns(2)

      with col1:
          st.metric('Initial GBP', f'£{initial_gbp}')
          st.metric('Final GBP', f'£{final_gbp}')

      with col2:
          if profit_loss > 0:
              st.metric('Profit/Loss', f'£{profit_loss:.2f}', delta_color='off')
              st.success('You earned a profit!')
          elif profit_loss < 0:
              st.metric('Profit/Loss', f'-£{abs(profit_loss):.2f}', delta_color='off')
              st.error('You had a loss')
          else:
              st.metric('Profit/Loss', 'Broke Even')


if __name__ == "__main__":
    main()
