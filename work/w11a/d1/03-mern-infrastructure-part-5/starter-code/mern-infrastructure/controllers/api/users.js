module.exports = {
  create
};

function create(req, res) {
  // Just a baby step
  res.json({
    name: req.body.name,
    email: req.body.email
  });
}