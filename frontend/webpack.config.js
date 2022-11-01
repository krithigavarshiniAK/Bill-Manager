const path = require("path");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = ({ mode } = { mode: "production" }) => {
    return {
        mode,
        entry: "./src/index.js",
        output: {
            publicPath: "auto",
            path: path.join(__dirname, "build"),
            filename: "index.bundle.js"
        },
        module: {
            rules: [
                {
                    test: /\.(js|jsx)$/,
                    exclude: /node_modules/,
                    loader: 'babel-loader',
                },
                {
                    test: /\.(ts|tsx)$/,
                    exclude: /node_modules/,
                    loader: 'babel-loader',
                },
                {
                    test: /\.css$/,
                    use: ['style-loader', 'css-loader'],
                },
                {
                    test: /\.svg$/,
                    issuer: /\.[jt]sx?$/,
                    use: ['@svgr/webpack', 'url-loader'],
                },
                {
                    test: /\.(png|jpe?g|gif|ico)$/,
                    exclude: /node_modules/,
                    use: ['file-loader?name=[name].[ext]']
                },
                {
                    test: /\.(yaml|yml)$/,
                    exclude: /node_modules/,
                    use: [
                        {
                            loader: 'js-yaml-loader'
                        }
                    ]
                },
            ],
        },
        plugins: [
            new HtmlWebpackPlugin({
                template: "./public/index.html"
            }),
            new webpack.HotModuleReplacementPlugin()
        ],
        devServer: {
            open: true,
            hot: true
        }
    }
};
