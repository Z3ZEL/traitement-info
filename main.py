import pandas as pd
import prince
data = pd.read_csv("res/nombre-origine.csv",encoding = 'utf-8')
# Check for missing values
null_values = data.isnull()
# Drop rows with missing values
data = data.dropna()



data_numbers = data.drop(columns=["Qualificatifs de données","Juridiction","Origine"], axis=1);
data_numbers.columns = ["Année","Nombre (nul)"]



pca = prince.PCA(
    n_components=2,
    n_iter=3,
    copy=True,
    check_input=True,
    engine='auto',
    random_state=42,
)

pca = pca.fit(data_numbers)

ax = pca.plot_row_coordinates(
    X=data_numbers,
    ax=None,
    figsize=(6, 6),
    x_component=0,
    y_component=1,
    color_labels=data["Origine"],
    labels=None,
    ellipse_outline=False,
    ellipse_fill=True,
    show_points=True
)


ax.get_figure().savefig('res/pca.png')
print(pca.column_correlations(data_numbers))

# mca = prince.MCA(
#     n_components=2,
#     n_iter=3,
#     copy=True,
#     check_input=True,
#     engine='auto',
#     random_state=42,
# )


# mca  = mca.fit(data_numbers)
# ax = mca.plot_coordinates(
#     X=data_numbers,
#     ax=None,
#     figsize=(6, 6),
#     show_row_points=True,
#     row_points_size=10,
#     show_row_labels=False,
#     show_column_points=True,
#     column_points_size=30,
#     show_column_labels=False,
#     legend_n_cols=1
# )

# ax.get_figure().savefig('res/pca.png')


# print(data_numbers.head())