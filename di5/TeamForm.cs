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
    public partial class TeamForm : Form
    {
        public TeamForm()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Visible = !richTextBox1.Visible; // Переключаем видимость
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox2.Visible = !richTextBox2.Visible; // Переключаем видимость
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
            MainForm mainForm = Application.OpenForms.OfType<MainForm>().FirstOrDefault();
            mainForm?.Show();
        }
    }
}
