const express = require("express");
const sql2 = require("mysql2");

const app = express();
const db = sql2.createConnection({
    user: "scorp_37",
    host: "db4free.net",
    password: "3V5*A4gUGVEHAkdq",
    database: "circuitsdatabase",
    port: 3306
});
app.use(express.json());

app.get('/fetch',(req,res)=>{
    db.query(
        'SELECT * FROM published_saves',
    (err,result)=>{
        if (err)
            res.send(err);
        else
            res.send(result);
    });
})

app.post('/post',(req,res)=>{
    const title = req.body.title;
    const data = req.body.data;

    const query = 'INSERT INTO published_saves (title,data) VALUES (?,?)';
    db.query(query, [title,data], (err, result) => {
        if (err) {
            console.error(err);
            return res.status(500).send('Error inserting data into the database');
        }
        console.log('Data has been inserted: ', result);
        res.json({ message: 'Data inserted successfully', id: result.insertId });
    });
})

const port = process.env.PORT || 3000
app.listen(port,()=>{console.log("Listening to "+port);})