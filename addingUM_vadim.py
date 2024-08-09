import pandas as pd
df = pd.read_csv('merged_stat_resp_viewable.csv')

#gave up on being concise 
df['um_hi_concentration'] = 10.**df['log_hi_conc'] * 10**6.
df['um_concentration'] = 10.**df['concentration'] * 10**6.
df['um_GI50'] = 10.**df['mean_GI50'] * 10**6.
df['um_IC50'] = 10.**df['mean_IC50'] * 10**6.
df['um_LC50'] = 10.**df['mean_LC50'] * 10**6.
df['um_TGI'] = 10.**df['mean_TGI'] * 10**6.


df.to_csv('merged_stat_UMresp_viewable.csv')