-- AfyaMkononi — Supabase schema
-- Run this ONCE in the Supabase SQL editor

-- Consultations: one row per completed session
create table if not exists consultations (
  id           uuid primary key default gen_random_uuid(),
  phone_hash   text not null,       -- SHA256 hash, not raw phone
  channel      text not null,       -- ussd | sms | app
  lang         text not null,       -- sw | en
  disease      text,                -- malaria | pneumonia | diarrhea | bp | other | null
  severity     text,                -- red | yellow | green | null
  advice_given text,
  created_at   timestamptz default now()
);

-- Feedback: did the user find the advice helpful?
create table if not exists feedback (
  id                uuid primary key default gen_random_uuid(),
  consultation_id   uuid references consultations(id),
  helpful           boolean not null,
  created_at        timestamptz default now()
);

-- Analytics view: disease counts per day (useful for dashboard)
create or replace view daily_analytics as
select
  date_trunc('day', created_at) as day,
  disease,
  channel,
  count(*) as total
from consultations
group by 1, 2, 3
order by 1 desc;

-- Indexes for performance
create index if not exists idx_consultations_created on consultations(created_at desc);
create index if not exists idx_consultations_disease  on consultations(disease);
