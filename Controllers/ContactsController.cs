using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using SQL.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace SQL.Controllers
{
    [ApiController]
    [Route("[controller]")]

    public class ContactsController:Controller
    {
        private ContactsContext _context;

        public ContactsController(ContactsContext context)
        {
            _context = context;
        } 

         [HttpGet]
        public ActionResult<IEnumerable<Contacts>> Get()
        {
            return _context.ContactsSet.ToList();
        }

        ~ContactsController(){
            _context.Dispose();
        }

    }
}