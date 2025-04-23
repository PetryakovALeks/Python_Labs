using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace di5
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void rasp_but_Click(object sender, EventArgs e)
        {
            new RaspForm().Show();
            this.Hide();
        }

        private void team_but_Click(object sender, EventArgs e)
        {
            // Кнопка состава команды
            new TeamForm().Show();
            this.Hide();
        }

        private void history_bat_Click(object sender, EventArgs e)
        {
            new historyForm().Show();
            this.Hide();
        }

        private void my_but_Click(object sender, EventArgs e)
        {
            // Кнопка состава команды
            new MyForm().Show();
            this.Hide();
        }

        private void Admin_but_Click(object sender, EventArgs e)
        {
            AdminLoginForm loginForm = new AdminLoginForm();
            if (loginForm.ShowDialog() == DialogResult.OK)
            {
                AdminPanelForm adminPanel = new AdminPanelForm();
                adminPanel.ShowDialog();
            }
        }
        private void MainForm_KeyDown(object sender, KeyEventArgs e)
        {
            
            if (e.KeyCode == Keys.F1)
            {
                new historyForm().ShowDialog();
                e.Handled = true;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            HelpForm helpForm = new HelpForm();
            helpForm.ShowDialog();
        }
    }
}

