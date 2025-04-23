using System;
using System.Drawing;
using System.Windows.Forms;

namespace di5
{
    public partial class AdminLoginForm : Form
    {
        public AdminLoginForm()
        {
            InitializeComponent();
            SetupUI();
        }

        private void SetupUI()
        {
            this.Text = "Авторизация администратора";
            this.Size = new Size(300, 200);
            this.StartPosition = FormStartPosition.CenterScreen;
            this.FormBorderStyle = FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;

            Label lblPassword = new Label
            {
                Text = "Пароль:",
                Location = new Point(20, 30),
                Size = new Size(100, 20)
            };

            TextBox txtPassword = new TextBox
            {
                Location = new Point(120, 30),
                Size = new Size(150, 20),
                PasswordChar = '*'
            };

            Button btnLogin = new Button
            {
                Text = "Войти",
                Location = new Point(100, 80),
                Size = new Size(100, 30),
                BackColor = Color.Salmon,
                ForeColor = Color.White
            };

            btnLogin.Click += (sender, e) =>
            {
                if (txtPassword.Text == "123") // В реальном приложении используйте безопасное хранение паролей
                {
                    this.DialogResult = DialogResult.OK;
                    this.Close();
                }
                else
                {
                    MessageBox.Show("Неверный пароль", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    txtPassword.Clear();
                }
            };

            this.Controls.AddRange(new Control[] { lblPassword, txtPassword, btnLogin });
            this.AcceptButton = btnLogin;
        }
    }
}