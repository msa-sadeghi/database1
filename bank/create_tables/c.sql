CREATE TABLE IF NOT EXISTS public.borrowers
(
    id integer NOT NULL DEFAULT nextval('borrowers_id_seq'::regclass),
    national_code character varying(10) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    father_name character varying(50) COLLATE pg_catalog."default",
    birth_date date,
    phone character varying(15) COLLATE pg_catalog."default" NOT NULL,
    mobile character varying(15) COLLATE pg_catalog."default",
    address text COLLATE pg_catalog."default",
    postal_code character varying(10) COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT borrowers_pkey PRIMARY KEY (id),
    CONSTRAINT borrowers_national_code_key UNIQUE (national_code)
);


CREATE TABLE IF NOT EXISTS public.guarantors
(
    id integer NOT NULL DEFAULT nextval('guarantors_id_seq'::regclass),
    loan_id integer,
    national_code character varying(10) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    phone character varying(15) COLLATE pg_catalog."default",
    address text COLLATE pg_catalog."default",
    relationship character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT guarantors_pkey PRIMARY KEY (id),
    CONSTRAINT guarantors_load_id_fkey FOREIGN KEY (loan_id)
        REFERENCES public.loans (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);

-- Table: public.installments

-- DROP TABLE IF EXISTS public.installments;

CREATE TABLE IF NOT EXISTS public.installments
(
    id integer NOT NULL DEFAULT nextval('installments_id_seq'::regclass),
    loan_id integer,
    installment_number integer NOT NULL,
    due_date date NOT NULL,
    amount numeric(15,2) NOT NULL,
    paid_amount numeric(15,2) DEFAULT 0,
    status character varying(20) COLLATE pg_catalog."default" DEFAULT 'pending'::character varying,
    paid_date date,
    delays_days integer DEFAULT 0,
    CONSTRAINT installments_pkey PRIMARY KEY (id),
    CONSTRAINT installments_loan_id_fkey FOREIGN KEY (loan_id)
        REFERENCES public.loans (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

-- Table: public.loans

-- DROP TABLE IF EXISTS public.loans;

CREATE TABLE IF NOT EXISTS public.loans
(
    id integer NOT NULL DEFAULT nextval('loans_id_seq'::regclass),
    borrower_id integer,
    loan_amount numeric(15,2) NOT NULL,
    installment_count integer NOT NULL,
    installment_amount numeric(15,2) NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    loan_type character varying(50) COLLATE pg_catalog."default",
    status character varying(20) COLLATE pg_catalog."default" DEFAULT 'active'::character varying,
    description text COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT loans_pkey PRIMARY KEY (id),
    CONSTRAINT loans_borrower_id_fkey FOREIGN KEY (borrower_id)
        REFERENCES public.borrowers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS public.payments
(
    id integer NOT NULL DEFAULT nextval('payments_id_seq'::regclass),
    installment_id integer,
    amounr numeric(15,2) NOT NULL,
    payment_date date NOT NULL,
    payment_method character varying(50) COLLATE pg_catalog."default",
    reference_number character varying(100) COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT payments_pkey PRIMARY KEY (id),
    CONSTRAINT payments_installment_id_fkey FOREIGN KEY (installment_id)
        REFERENCES public.installments (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    username character varying(50) COLLATE pg_catalog."default" NOT NULL,
    password_hash character varying(255) COLLATE pg_catalog."default" NOT NULL,
    full_name character varying(100) COLLATE pg_catalog."default",
    role character varying(20) COLLATE pg_catalog."default" DEFAULT 'operator'::character varying,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_username_key UNIQUE (username)
)


