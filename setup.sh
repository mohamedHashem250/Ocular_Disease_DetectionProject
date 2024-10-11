mkdir -p ~/.streamlit/

# Configure credentials.toml
echo "\
[general]\n\
email = \"mohamedahashem250@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

# Configure config.toml
echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
" > ~/.streamlit/config.toml