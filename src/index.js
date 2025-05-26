require('dotenv').config();
const express = require('express');
const axios = require('axios');
const url = require('url');

const port = process.env.port || 4000;
const app = express();

app.get('/api/auth/discord/redirect', async (req, res) => {
    const { code } = req.query;

    if (code) {
        const formData = new url.URLSearchParams({
            client_id: process.env.client_id, // lowercase
            client_secret: process.env.client_secret,
            grant_type: 'authorization_code',
            code: code.toString(),
            redirect_uri: 'http://localhost:4000/api/auth/discord/redirect', // lowercase
        });

        try {
            const output = await axios.post(
                'https://discord.com/api/oauth2/token',
                formData.toString(),
                {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                }
            );

            if (output.data && output.data.access_token) {
                // Use Bearer token to get user info
                const userInfo = await axios.get('https://discord.com/api/users/@me', {
                    headers: {
                        Authorization: `Bearer ${output.data.access_token}`
                    }
                });

                res.json({
                    token: output.data,
                    user: userInfo.data
                });
            } else {
                res.status(400).json({ error: 'No data received from Discord.' });
            }
        } catch (err) {
            res.status(500).json({ error: 'Failed to exchange code for token or fetch user info.', details: err.message });
        }
    } else {
        res.status(400).json({ error: 'No code provided in query.' });
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});     