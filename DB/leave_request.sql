--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: division; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.division (
    division_code character varying(10) NOT NULL,
    division_name character varying(100) NOT NULL
);


ALTER TABLE public.division OWNER TO postgres;

--
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    staff_id character varying(15) NOT NULL,
    staff_name character varying(100) NOT NULL,
    user_id character varying(30) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(100) NOT NULL,
    supervisor_user_id character varying(30) NOT NULL,
    sex character varying(1) NOT NULL,
    division_code character varying(10) NOT NULL,
    unit_code character varying(10) NOT NULL,
    location character varying(30) NOT NULL,
    "position" character varying(150) NOT NULL,
    joined_date date NOT NULL,
    expat bit(1) NOT NULL,
    contract bit(1) NOT NULL,
    balance double precision NOT NULL
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- Name: history_leave; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.history_leave (
    leave_id integer NOT NULL,
    staff_id character varying(15) NOT NULL,
    supervisor_user_id character varying(30) NOT NULL,
    leave_type character varying(100) NOT NULL,
    start_date date NOT NULL,
    start_date_length double precision NOT NULL,
    end_date date NOT NULL,
    end_date_length double precision NOT NULL,
    number_of_leave_days double precision NOT NULL,
    requestor_remarks text NOT NULL,
    submission_date date NOT NULL,
    approval_status bit(1),
    approval_remarks text,
    approval_date date
);


ALTER TABLE public.history_leave OWNER TO postgres;

--
-- Name: history_leave_leave_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.history_leave_leave_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.history_leave_leave_id_seq OWNER TO postgres;

--
-- Name: history_leave_leave_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.history_leave_leave_id_seq OWNED BY public.history_leave.leave_id;


--
-- Name: holiday; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.holiday (
    holiday_id integer NOT NULL,
    holiday_name character varying(100) NOT NULL,
    holiday_date date
);


ALTER TABLE public.holiday OWNER TO postgres;

--
-- Name: holiday_holiday_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.holiday_holiday_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.holiday_holiday_id_seq OWNER TO postgres;

--
-- Name: holiday_holiday_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.holiday_holiday_id_seq OWNED BY public.holiday.holiday_id;


--
-- Name: leave; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.leave (
    leave_id integer NOT NULL,
    leave_name character varying(100) NOT NULL,
    entitlement double precision,
    sex character varying(1)
);


ALTER TABLE public.leave OWNER TO postgres;

--
-- Name: leave_leave_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.leave_leave_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.leave_leave_id_seq OWNER TO postgres;

--
-- Name: leave_leave_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.leave_leave_id_seq OWNED BY public.leave.leave_id;


--
-- Name: unit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.unit (
    unit_code character varying(10) NOT NULL,
    unit_name character varying(100) NOT NULL,
    division_name character varying
);


ALTER TABLE public.unit OWNER TO postgres;

--
-- Name: history_leave leave_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_leave ALTER COLUMN leave_id SET DEFAULT nextval('public.history_leave_leave_id_seq'::regclass);


--
-- Name: holiday holiday_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.holiday ALTER COLUMN holiday_id SET DEFAULT nextval('public.holiday_holiday_id_seq'::regclass);


--
-- Name: leave leave_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.leave ALTER COLUMN leave_id SET DEFAULT nextval('public.leave_leave_id_seq'::regclass);


--
-- Data for Name: division; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.division (division_code, division_name) FROM stdin;
DC-FED	Front End Division
DC-BED	Back End Division
DC-BDD	Database Division
DC-DRTR	Direktur
\.


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee (staff_id, staff_name, user_id, email, password, supervisor_user_id, sex, division_code, unit_code, location, "position", joined_date, expat, contract, balance) FROM stdin;
DC-BED-01-00	Vian Unyu	vianvian	vianvian@test.com	123	DC-DRTR-00-00	P	DC-BED	BED-U01	Pusat	Manager Back End Dev	2019-04-01	0	0	60
DC-BED-01-05	Tika Latami	laktamil	laktamil@test.com	123	DC-BED-01-00	W	DC-BED	BED-U01	Pusat	Senior Back End Dev	2018-04-05	0	0	12
DC-BED-01-02	Danur Unyu	danurunyu	danurunyu@test.com	123	DC-BED-01-00	W	DC-BED	BED-U01	Pusat	Senior Back End Dev	2019-03-30	0	0	20
DC-BED-01-03	Bayu Unyu	Bayuunyu	Bayuunyu@test.com	123	DC-BED-01-00	P	DC-BED	BED-U01	Pusat	Senior Back End Dev	2019-03-30	0	0	5.5
DC-BED-01-01	Aditya ABU	adityaabu	adityaabu@test.com	123	DC-BED-01-00	P	DC-BED	BED-U01	Pusat	Senior Back End Dev	2019-03-30	0	0	19.5
\.


--
-- Data for Name: history_leave; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.history_leave (leave_id, staff_id, supervisor_user_id, leave_type, start_date, start_date_length, end_date, end_date_length, number_of_leave_days, requestor_remarks, submission_date, approval_status, approval_remarks, approval_date) FROM stdin;
5	DC-BED-01-03	DC-BED-01-00	Cuti Pernikahan	2019-03-28	1	2019-04-02	1	4	Cuti Pernikahan	2019-03-30	1	123321213	2019-04-04
1	DC-BED-01-01	DC-BED-01-00	Cuti Sakit	2019-04-01	1	2019-04-03	1	3	Demam Tinggi	2019-03-30	1	Ok, semoga lekas sembuh.	2019-03-30
34	DC-BED-01-03	DC-BED-01-00	Cuti Kematian Istri / Suami / Anak / Orang Tua / Mertua	2019-04-09	0.25	2019-04-10	0.25	0.5	e	2019-04-08	1	ok	2019-04-08
35	DC-BED-01-03	DC-BED-01-00	Cuti Anak Menikah	2019-04-10	0.25	2019-04-12	0.25	1.5	1	2019-04-08	0	tidak	2019-04-08
36	DC-BED-01-00	DC-DRTR-00-00	Cuti Istri Hamil	2019-04-07	0.25	2019-04-08	0.25	-0.5	u	2019-04-08	\N	\N	\N
37	DC-BED-01-01	DC-BED-01-00	Cuti Istri Hamil	2019-04-10	0.25	2019-04-11	0.25	0.5	istri hamil	2019-04-08	1	OK	2019-04-08
2	DC-BED-01-01	DC-BED-01-00	Cuti Sakit	2019-04-10	1	2019-04-11	1	1	Sakit Gigi	2019-03-30	1	Ok, selamat menempuh hidup baru.	2019-03-30
30	DC-BED-01-01	DC-BED-01-00	Cuti Istri Hamil	2019-04-11	0.25	2019-04-19	0.25	5.5	1	2019-04-04	\N	\N	\N
31	DC-BED-01-01	DC-BED-01-00	Cuti Istri Hamil	2019-04-11	0.25	2019-04-19	0.25	5.5	1	2019-04-04	\N	\N	\N
3	DC-BED-01-03	DC-BED-01-00	Cuti Pernikahan	2019-04-10	1	2019-04-13	1	7	Cuti Pernikahan	2019-03-30	0	Ok, selamat menempuh hidup baru.	2019-04-04
\.


--
-- Data for Name: holiday; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.holiday (holiday_id, holiday_name, holiday_date) FROM stdin;
26	Tahun Baru 2019 Masehi	2019-01-01
27	Tahun Baru Imlek 2570	2019-02-05
28	Hari Raya Nyepi Tahun Baru Saka 1941	2019-03-07
29	Isra Mikraj Nabi Muhammad SAW	2019-04-03
30	Wafat Isa Al Masih	2019-04-19
31	Hari Buruh Internasional	2019-05-01
32	Hari Raya Waisak 2563	2019-05-19
33	Kenaikan Isa Al MAsih	2019-05-30
34	Hari Lahir Pancasila	2019-06-01
35	Cuti Bersama Hari Raya Idul Fitri 1440 Hijriyah	2019-05-03
36	Cuti Bersama Hari Raya Idul Fitri 1440 Hijriyah	2019-05-04
37	Hari Raya Idul Fitri 1440 Hijriyah	2019-05-05
38	Hari Raya Idul Fitri 1440 Hijriyah	2019-05-06
39	Cuti Bersama Hari Raya Idul Fitri 1440 Hijriyah	2019-05-07
40	Hari Raya Idul Adha 1440 Hijriyah	2019-08-11
41	Hari Kemerdekaan Republik Indonesia	2019-08-17
42	Tahun Baru Islam 1441 Hijriyah	2019-09-01
43	Maulid Nabi Muhammad SAW	2019-11-09
44	Cuti Bersama Hari Raya Natal	2019-12-24
45	Hari Raya Natal	2019-12-25
\.


--
-- Data for Name: leave; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.leave (leave_id, leave_name, entitlement, sex) FROM stdin;
1	Cuti Hamil	90	W
2	Cuti Keguguran	45	W
3	Cuti Menstruasi	2	W
4	Cuti Istri Hamil	2	P
5	Cuti Pernikahan	3	\N
6	Cuti Anak Menikah	2	\N
7	Cuti Kematian Istri / Suami / Anak / Orang Tua / Mertua	2	\N
8	Cuti Kematian Kakek, Nenek	1	\N
9	Cuti Kematian Saudara atau Keluarga yang terdaftar di kartu keluarga	1	\N
10	Ibadah Haji	\N	\N
11	Permintaan dari Pemerintah / Pengadilan / Kepolisian	\N	\N
12	Cuti Sakit	\N	\N
\.


--
-- Data for Name: unit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.unit (unit_code, unit_name, division_name) FROM stdin;
FED-U01	Front End Unit 01	Front End Division
FED-U02	Front End Unit 02	Front End Division
BED-U01	Back End Unit 01	Back End Division
BED-U02	Back End Unit 02	Back End Division
BDD-U01	Database Unit 01	Database Division
BDD-U02	Database Unit 02	Database Division
DRTR-00	Direktur	Direktur
\.


--
-- Name: history_leave_leave_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.history_leave_leave_id_seq', 37, true);


--
-- Name: holiday_holiday_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.holiday_holiday_id_seq', 45, true);


--
-- Name: leave_leave_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.leave_leave_id_seq', 12, true);


--
-- Name: division division_division_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.division
    ADD CONSTRAINT division_division_name_key UNIQUE (division_name);


--
-- Name: division division_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.division
    ADD CONSTRAINT division_pkey PRIMARY KEY (division_code);


--
-- Name: employee employee_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_email_key UNIQUE (email);


--
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (staff_id);


--
-- Name: employee employee_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_user_id_key UNIQUE (user_id);


--
-- Name: history_leave history_leave_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_leave
    ADD CONSTRAINT history_leave_pkey PRIMARY KEY (leave_id);


--
-- Name: holiday holiday_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.holiday
    ADD CONSTRAINT holiday_pkey PRIMARY KEY (holiday_id);


--
-- Name: leave leave_leave_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.leave
    ADD CONSTRAINT leave_leave_name_key UNIQUE (leave_name);


--
-- Name: leave leave_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.leave
    ADD CONSTRAINT leave_pkey PRIMARY KEY (leave_id);


--
-- Name: unit unit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.unit
    ADD CONSTRAINT unit_pkey PRIMARY KEY (unit_code);


--
-- Name: unit unit_unit_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.unit
    ADD CONSTRAINT unit_unit_name_key UNIQUE (unit_name);


--
-- Name: employee employee_division_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_division_code_fkey FOREIGN KEY (division_code) REFERENCES public.division(division_code);


--
-- Name: employee employee_unit_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_unit_code_fkey FOREIGN KEY (unit_code) REFERENCES public.unit(unit_code);


--
-- Name: history_leave history_leave_leave_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_leave
    ADD CONSTRAINT history_leave_leave_type_fkey FOREIGN KEY (leave_type) REFERENCES public.leave(leave_name);


--
-- Name: history_leave history_leave_staff_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_leave
    ADD CONSTRAINT history_leave_staff_id_fkey FOREIGN KEY (staff_id) REFERENCES public.employee(staff_id);


--
-- Name: unit unit_division_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.unit
    ADD CONSTRAINT unit_division_name_fkey FOREIGN KEY (division_name) REFERENCES public.division(division_name);


--
-- PostgreSQL database dump complete
--

