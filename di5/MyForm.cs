using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace di5
{
    public partial class MyForm : Form
    {
        public MyForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Visible = !richTextBox1.Visible; // Переключаем видимость
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox2.Visible = !richTextBox2.Visible; // Переключаем видимость
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MainForm mainForm = Application.OpenForms.OfType<MainForm>().FirstOrDefault();
            if (mainForm == null)
            {
                mainForm = new MainForm();
            }
            mainForm.Show();
            this.Close();
        }
    }
}
